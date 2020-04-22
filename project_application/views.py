from django.shortcuts import render

from django.http import HttpResponseRedirect

from .forms import NewBusiness, NewNewsletterSubscriber
from .models import Business

from random import shuffle

# Create your views here.
def main(request):
    businesses_list = Business.objects.order_by('?')
    businesses_dict = {'businesses':businesses_list}
    return render(request, "project_application/main.html",context=businesses_dict)

def wspierampl(request):
    return render(request, "project_application/wspierampl.html")

def businesses(request):
    form = NewBusiness()
    if request.method == "POST":
        form = NewBusiness(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return main(request)
        else:
            print("Form error!")
    return render(request, 'project_application/form.html', {'form':form})

def about(request):
    return render(request, 'project_application/about.html')

def contact(request):
    news_form = NewNewsletterSubscriber()

    if request.method == "POST":
        news_form = NewNewsletterSubscriber(request.POST)

        if news_form.is_valid():
            news_form.save(commit=True)
            news_form = NewNewsletterSubscriber()
            return render(request, "project_application/contact.html", {'news_form':news_form})
        else:
            print("Form error!")
    return render(request, "project_application/contact.html", {'news_form':news_form})

def explore(request):
    return render(request, 'project_application/explore.html')
