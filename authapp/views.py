from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from authapp.models import Contact


# Create your views here.
def Home(request):
    return render(request,"index.html")

def signup(request):
    if request.method=="POST":
        username=request.POST.get('usernumber')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
      
        if len(username)>10 or len(username)<10:
            messages.info(request,"Phone Number Must be 10 Digits")
            return redirect('/signup')

        if pass1!=pass2:
            messages.info(request,"Password is not Matching")
            return redirect('/signup')
       
        try:
            if User.objects.get(username=username):
                messages.warning(request,"Phone Number is Taken")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
        
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
        
        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"User is Created Please Login")
        return redirect('/login')
        
        
    return render(request,"signup.html")

def handlelogin(request):
    if request.method=="POST":        
        username=request.POST.get('usernumber')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successful")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')
            
        
    return render(request,"handlelogin.html")

def handleLogout(request):
    logout(request)
    messages.success(request,"Logout Success")    
    return redirect('/login')


def contact(request):
    if request.method=="POST":
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        number=request.POST.get('num')
        desc=request.POST.get('desc')
        myquery=Contact(name=name,email=email,phonenumber=number,description=desc)
        myquery.save()       
        messages.info(request,"Thanks for Contacting us we will get back you soon")
        return redirect('/contact')
        
    return render(request,"contact.html")


def counter(request):
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': 'kiu32HX3Dm3InU1y3ymTRQ==kWYXbZsYQpaFpDKX'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'counter.html', {'api': api})
    else:
        return render(request, 'counter.html', {'query': 'Enter a valid query'})
    


def workout(request):
    import requests
    import json
    if request.method == 'POST':
        muscle = request.POST['muscle']
        api_url = 'https://api.api-ninjas.com/v1/exercises?muscle='
        api_request = requests.get(
            api_url + muscle, headers={'X-Api-Key': 'kiu32HX3Dm3InU1y3ymTRQ==kWYXbZsYQpaFpDKX'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'workout.html', {'api': api})
    else:
        return render(request, 'workout.html', {'muscle': 'Enter a valid muscle'})
    

def calculate_calories(request):
    if request.method == 'POST':
        age = int(request.POST.get('age'))
        weight = float(request.POST.get('weight'))
        heart_rate = float(request.POST.get('heart_rate'))
        time = float(request.POST.get('time'))
        
        calories = ((age * 0.2757) + (weight * 2.20462 * 0.03295) + (heart_rate * 1.0781) - 75.4991) * time / 8.368
        calories = round(calories, 2)
        
        return render(request, 'calculate_calories.html', {'calories': calories})
    return render(request, 'calculate_calories.html')