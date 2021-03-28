from portfolio_blog.forms import ContactForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

def home(request):
    return render(request, 'pages/about-me.html')

def about(request):
    return render(request, 'pages/about.html')

def projects(request):
    return render(request, 'pages/projects.html')

def contact(request):
    return render(request, 'pages/contact.html')

