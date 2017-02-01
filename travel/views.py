from django.shortcuts import render
from travel.forms import ContactForm

def index (request):
        return render(request,'index.html')
def services (request):
        return render(request,'services.html')  
def exotics(request):
        return render (request,'exotics.html')
def whatsyourwish(request):
        return render (request,'whatsyourwish.html')
def hoppers(request):
        return render (request,'hoppers.html')
def flights(request):
        return render (request,'flights.html')
def hotels(request):
        return render (request,'hotels.html')
def travlino(request):
        return render (request,'travlino.html')
def contact(request):
        form_class = ContactForm
        return render (request,'contact.html', {
        'form': form_class,
    })    
def membership(request):
        return render (request,'membership.html')
def membershiplans(request):
        return render (request,'membershipplans.html')
def login(request):
        return render (request,'login.html')
def signup(request):
        return render (request,'signup.html')
def corporate(request):
        return render (request,'corporate.html')
def contact_form(request):
        return render (request,'contact_form.html')