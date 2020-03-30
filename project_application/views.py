from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'project_application/main.html')

def about(request):
    return render(request, 'project_application/about.html')

def contact(request):
    return render(request, 'project_application/contact.html')
