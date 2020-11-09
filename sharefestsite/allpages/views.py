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