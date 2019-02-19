import pyrebase
from django.shortcuts import render
from django.contrib import auth
config = {
    'apiKey' : "AIzaSyAxl6eKJhU3lZKIUECJQdaoYoUQ6y9e2sc",
    'authDomain' : "indiahealth-2e534.firebaseapp.com",
    'databaseURL' : "https://indiahealth-2e534.firebaseio.com",
    'projectId' : "indiahealth-2e534",
    'storageBucket' : "indiahealth-2e534.appspot.com",
    'messagingSenderId' : "136387651389"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()



def signIn(request):
    return render(request, "signIn/signIn.html")

def postsign(request):
    email=request.POST.get("sign-in-uid")
    passw = request.POST.get("sign-in-pwd")
    try:
        user = authe.sign_in_with_email_and_password(email,passw)
    except:
        message="Invalid Credentials Try Again"
        return render(request,"signIn/signIn.html",{"msg":message})
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    name = database.child('users').child(a).child('details').child('name').get().val()
    return render(request, 'home/home.html', {'e': name})


def postsignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    pwd = request.POST.get('pwd')
    c_pwd = request.POST.get('c_pwd')

    try:
        user = authe.create_user_with_email_and_password(email, pwd)
        uid = user['localId']

        data = {"name": name, "status": "1"}
        database.child("users").child(uid).child("details").set(data)
    except Exception as e:
        message = "Unable to create account try again"
        return render(request, "signIn/signIn.html", {"msg": e})
    message = "Account created Succesfully"
    return render(request, "signIn/signIn.html", {"msg": message})



def logout(request):
    auth.logout(request)
    return signIn(request)