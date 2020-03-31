from django.shortcuts import render

from .forms import NewBusiness, NewNewsletterSubscriber
from .models import Business

# Create your views here.
def main(request):
    businesses_list = Business.objects.order_by('update_date')
    businesses_dict = {'businesses':businesses_list}
    return render(request, "project_application/main.html",context=businesses_dict)

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
    return render(request, 'project_application/contact.html')

def explore(request):
    return render(request, 'project_application/explore.html')
