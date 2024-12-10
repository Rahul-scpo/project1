from django.shortcuts import render
from app_13.models import logintable,personaltable,usertable
from django.http import HttpResponse
# Create your views here.

def signup(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]

        x = logintable(Name=a, Email=b, Type="User")
        x.save()
        q = usertable(Loginid=x,Name=a, Email=b,Type="User")
        q.save()
        return  HttpResponse("signed in successfully")
    return render(request, "signup.html")

def login(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]

        q = logintable.objects.filter(Name=a).first()

        if q and q.Email == b and q.Type == "User":
            x = usertable.objects.get(Name=a)

            if x.Email == b:
                request.session["member_id"] = x.id
                return render(request, "profile.html", {"name": x, "email": b})
        else:
            return HttpResponse("invalid username and password")

    return render(request, "login.html")

def personal(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]
        c = request.POST["name3"]
        d = request.POST["name4"]
        e = request.POST["name5"]
        f = request.POST["name6"]
        g = request.POST["name7"]

        k = personaltable(Name=a, lastname=b, dob=c, age=d, address=e, Email=f, number=g)
        k.save()
        return HttpResponse("successfully submitted")

    return render(request, "personalform.html")

def personaldata(request):

    x = usertable.objects.get(id=request.session["member_id"])
    print(x.Name)
    c=personaltable.objects.filter(Name=x.Name)

    if request.method=="POST":
        c.Name = request.POST["name1"]
        c.lastname = request.POST["name2"]
        c.dob = request.POST["name3"]
        c.age = request.POST["name4"]
        c.address = request.POST["name5"]
        c.Email = request.POST["name6"]
        c.number = request.POST["name7"]
        c.save()

    return render(request, "data_personal.html",{"personalkey":c})