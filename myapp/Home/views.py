from django.shortcuts import render,HttpResponse

# Create your views here.
def Home(request):
    l = ["Ajay","Shubham","Sahil","Naman"]
    return render(request, 'Home.html',{"Data":l})