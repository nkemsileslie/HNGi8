from django.http import request
from django.shortcuts import render
from cv.models import contactform 

# the main page
def web(request):
    return render(request, 'cv/web.html')

# the Data from the contact me form
def form(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        city = request.POST['city']
        mobile = request.POST['mobile']
        message = request.POST['message'] 

        print(name, email, mobile, city, message)

        ins =contactform(name=name, email=email,city=city,mobile=mobile,message=message)
        ins.save()

        print(name, email, mobile, city, message)
        print("Data has been saved to the database")
    return render(request, 'cv/webform.html')
 