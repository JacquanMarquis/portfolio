from django.shortcuts import render, HttpResponse
from home.models import Contact

def home(request):
    #return HttpResponse("This is my homepage (/)")
    context = {'name': 'Harry', 'course': 'Django'}
    return render(request, 'home.html', context)

def about(request):
   #return HttpResponse("This is my about page (about)")
   aboutMe = {'birthday': 'June 21, 1988', 'heart': 'Winner'}
   return render(request, 'about.html', aboutMe)


def projects(request):
    # return HttpResponse("This is my project page (project)")
    return render(request, 'projects.html')


def contact(request):
    # return HttpResponse("This is my contact page (contact)")
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        #print(name, phone, email, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print('the data has been written to the db')

    return render(request, 'contact.html')














