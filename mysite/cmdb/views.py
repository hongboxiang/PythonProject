from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models

# Create your views here.
def index(request):
    # return HttpResponse("hello world")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        models.UserInfo.objects.create(user=username, pwd=password)
    user_list = models.UserInfo.objects.all()
    return render(request, "index.html", {"data":user_list})
