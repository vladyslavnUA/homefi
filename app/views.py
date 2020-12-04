from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'app/listings.html', context)

def about(request):
    context = {}
    return render(request, 'app/about.html', context)

def detail(request):
    context = {}
    return render(request, 'app/detail.html', context)