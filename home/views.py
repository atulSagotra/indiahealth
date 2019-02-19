from django.shortcuts import render

# Create your views here.
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

def date_time():
    import datetime
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return date_time


def home(request):
    return render(request, "home/home.html")

def doctordetails(request):

    return render(request,'home/doctor.html')

def profile(request):
    return render(request, 'home/profile.html')

def post_create(request):

    import time
    from datetime import datetime, timezone
    import pytz

    tz= pytz.timezone('Asia/Kolkata')
    time_now= datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))
    doctorName = request.POST.get('doctor name')
    doctorNum =request.POST.get('doctor num')
    doctorEmail = request.POST.get('doctor email')
    doctorExp = request.POST.get('doctor exp')
    doctorGender = request.POST.get('doctor gender')
    doctorSpl = request.POST.get('doctor speciality')

    idtoken= request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    data = {
        "doctorName":doctorName,
        "doctorNum":doctorNum,
        "doctorEmail":doctorEmail,
        "doctorExp":doctorExp,
        "doctorGender":doctorGender,
        "doctorspl":doctorSpl,
        "lastUpdated": date_time(),
    }
    database.child('users').child(a).child('DoctorDetails').child(millis).set(data)
    name = database.child('users').child(a).child('details').child('name').get().val()
    return render(request,'home/home.html', {'e':name})


def postprofile(request):
    hospitalName = request.POST.get('hospital name')
    hospitalNum = request.POST.get('hospital num')
    hospitalEmail = request.POST.get('hospital email')
    hospitalAddress = request.POST.get('hospital address')
    hospitalServices = request.POST.get('hospital services')
    hospitalChair = request.POST.get('hospital chair')
    hospitalChairNum = request.POST.get('hospital chair num')
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    data = {"hospitalname": hospitalName,
            "hospitalNum": hospitalNum,
            "hospitalEmail": hospitalEmail,
            "hospitalAddress": hospitalAddress,
            "hospitalServices": hospitalServices,
            "hospitalChair": hospitalChair,
            "hospitalChairNum": hospitalChairNum,
            "lastupdated":date_time()
            }
    database.child("users").child(a).child("details").set(data)
    return render(request ,"home/home.html")
