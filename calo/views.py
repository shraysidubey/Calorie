from django.shortcuts import render
from django.http import HttpResponse
from calo.forms import UserForm, UserProfileForm, Food_qtyForm, ActivityForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from calo.models import UserProfile, Activity, Food_qty
import requests, json
import datetime as DT

def index(request):

    context_dict = {}

    if request.user.is_authenticated():
        user_profile = UserProfile.objects.get(user=request.user.id)
        context_dict['user_profile'] = user_profile

        if request.method == 'POST' and 'food_submit' in request.POST:
            form = Food_qtyForm(request.POST)

            if form.is_valid():
                user_profile = UserProfile.objects.get(user= request.user.id)
                food = form.save(commit=False)
                food.calories = get_Calories(food.food_consume)
                context_dict['calorie_change'] = "+" + str(food.calories)
                food.user = user_profile
                food.save()

        context_dict['form'] = Food_qtyForm()

        if request.method == 'POST' and "activity_submit" in request.POST:
            form = ActivityForm(request.POST)
            if form.is_valid():
                user_profile = UserProfile.objects.get(user=request.user.id)
                activity = form.save(commit=False)                              #form alreadt contain exercise and & its object has
                activity.calories_burned = burned_calorie(user_profile,activity)
                context_dict['calorie_change1'] = "-" + str(activity.calories_burned)
                activity.user = user_profile
                activity.save()

        context_dict['form1'] = ActivityForm()

        context_dict['activity_date_dict'] = history_of_calorieburned(user_profile)

        context_dict['history_of_calorie'] = history_of_calorie_consumed(user_profile)

        context_dict['all_history'] = all_history(user_profile)

    return render(request, 'calo/index.html', context_dict)

def register(request):

    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'calo/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:

                login(request, user)
                return HttpResponseRedirect('/calo/')
            else:
                return HttpResponse("Your Calorie counter account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:

        return render(request, 'calo/login.html', {})

def some_view(request):
    if not request.user.is_authenticated():
        return HttpResponse("You are logged in.")
    else:
        return HttpResponse("You are not logged in.")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/calo/')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/calo/')

def profile(request, user_id):

    context_dict = {}

    try:
        user_profile = UserProfile.objects.get(id=user_id)
        context_dict['user'] = user_profile
        print("298759827598275")
        print(user_profile.id)
        print("298759827598275")

    except UserProfile.DoesNotExist:
        print("UserNot found")
        pass
    return render(request, 'calo/profile.html', context_dict)


def get_Calories(food_consume):
    url = "https://edamam-edamam-nutrition-analysis.p.rapidapi.com/api/nutrition-data"

    querystring = {"ingr": food_consume}

    headers = {'x-rapidapi-host': "edamam-edamam-nutrition-analysis.p.rapidapi.com",
               'x-rapidapi-key': "803c702c04msh767a6ffe9232ddap17d2b7jsn376522bffba6"}

    response = requests.request("GET", url, headers=headers, params=querystring)

    food_dict = json.loads(response.text)

    return food_dict['calories']


def burned_calorie(user_ptofile, activity):

    querystring={}

    querystring['height_cm']=user_ptofile.Height
    querystring['weight_kg']=user_ptofile.Weight
    querystring['age']=user_ptofile.age
    querystring['gender']=user_ptofile.gender
    querystring['query']=activity.exercise                   #take if from FORM

    url = "https://trackapi.nutritionix.com/v2/natural/exercise/"

    #querystring = {'query': "ran 3 miles","gender":"female","weight_kg":"72.5","height_cm":"167.64","age":"30"}

    headers = {'x-app-id': "6b0ac11b",'x-app-key': "3bb8f07dbf982337da050c09e23f96f1"}

    response = requests.post(url, headers=headers, data=querystring)

    activity_dict = json.loads(response.text)
    A = activity_dict['exercises']
    K = (A[0])
    return K['nf_calories']

def history_of_calorieburned(user_profile):
    today = DT.date.today()
    week_ago = today - DT.timedelta(days=7)
    pre_record = Activity.objects.filter(user=user_profile).filter(date_added__gte=week_ago)
    dat_dict = {}
    for i in pre_record:
        temp_date = i.date_added
        dat_key = str(temp_date.date())
        if dat_key not in dat_dict:
            dat_dict[dat_key] = i.calories_burned
        else:
            dat_dict[dat_key] += i.calories_burned
    return dat_dict


def history_of_calorie_consumed(user_profile):
    today = DT.date.today()
    week_ago = today - DT.timedelta(days=7)
    pre_record = Food_qty.objects.filter(user=user_profile.id).filter(date_added__gte=week_ago)
    dat_dict = {}
    for i in pre_record:
        temp_date = i.date_added
        dat_key = str(temp_date.date())
        if dat_key not in dat_dict:
            dat_dict[dat_key] = i.calories
        else:
            dat_dict[dat_key] += i.calories
    return dat_dict

def all_history(user_profile):

    P = {}
    today = DT.date.today()
    week_ago = today - DT.timedelta(days=2)
    pre_record1 = Food_qty.objects.filter(user=user_profile.id).filter(date_added__gte=week_ago)
    pre_record2 = Activity.objects.filter(user=user_profile).filter(date_added__gte=week_ago)
    P['food_list'] = pre_record1
    P['calories'] = pre_record1
    P['activity_list'] = pre_record2

    return P

