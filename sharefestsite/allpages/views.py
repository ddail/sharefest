from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'allpages/index.html')

def about_view(request):
    return render(request, 'allpages/about.html')

def connect_view(request):
    return render(request, 'allpages/connect.html')

def map_view(request):
    return render(request, 'allpages/mappage.html')
    
def donate_view(request):
    return render(request, 'allpages/donate.html')

def volunteer_view(request):
    return render(request, 'allpages/volunteer.html')

def login_view(request):
    return render(request, 'allpages/login.html')