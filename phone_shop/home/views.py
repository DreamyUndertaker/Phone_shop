from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html')
def catalog(request):
    return render(request, 'home/catalog.html')
def about(request):
    return render(request, 'home/about.html')
def shipping(request):
    return render(request, 'home/shipping.html')
def blog(request):
    return render(request, 'home/blog.html')
def contacts(request):
    return render(request, 'home/contacts.html')