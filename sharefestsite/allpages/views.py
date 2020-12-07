from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from sharefestsite.settings import EMAIL_HOST_USER
from allpages.forms import EmailForm
from . import forms
from .models import Users
from django.conf import settings
#from django.contrib.auth.models import User

def home_view(request):
    return render(request, 'allpages/index.html')

def about_view(request):
    return render(request, 'allpages/about.html')

def connect_view(request):
    return render(request, 'allpages/connect.html')

def user_info(request):
    context = {}
    context["dataset"] = Users.objects.all()
    return render(request, 'allpages/user_info.html', context)

def contact(request):
    #sub = forms.EmailForm()
    if request.method == 'GET':
        sub = EmailForm()
    else:
        sub = forms.EmailForm(request.POST)
        if sub.is_valid():
            #recievers = []
            #for user in Users.objects.all():
            #    recievers.append(user.email)
            subj = sub.cleaned_data['subject']
            memo = sub.cleaned_data['message']
            recepient = str(sub['Emails'].value())
            #user_email = User.objects.get('email')
            #recipient_list = [user_email]
            
            send_mail(subj, memo, EMAIL_HOST_USER, [recepient], fail_silently= False)
            #send_mail(subj, memo, EMAIL_HOST_USER, recipient_list)

        return render(request, 'allpages/success.html', {'recepient': recepient})
    return render(request, 'allpages/contact.html', {'form': sub})

#def thanks(request):
 #   return HttpResponse('Thank you for your message.')

def success_view(request):
    return(request, 'allpages/success.html')

def map_view(request):
    return render(request, 'allpages/mappage.html')
    
def donate_view(request):
    return render(request, 'allpages/donate.html')

def volunteer_view(request):
    return render(request, 'allpages/volunteer.html')
