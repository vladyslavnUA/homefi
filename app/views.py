from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
def home(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    for i in listings:
        print(i.id)
    return render(request, 'app/listings.html', context)

def about(request):
    context = {}
    return render(request, 'app/about.html', context)

def detail(request, id):
    listing = Listing.objects.get(id=id)
    context = {
        'listing': listing
    }
    return render(request, 'app/detail.html', context)

def single(request, id):
    house = Listing.objects.get(id=id)
    context = {
        'house': house
    }
    
    return render(request, 'app/detail.html', context)

# @login_required
def new_listing(request):
    form = ListingForm()
    user = request.user
    print(user)
    if not user.is_authenticated:
        return redirect('users:login')
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        all_images = request.FILES.getlist('images')
        if form.is_valid():
            obj = form.save(commit=False)
            # title, description, start_time, end_time, send_to
            obj.address = request.POST.get('address')
            obj.city = request.POST.get('city')
            obj.state = request.POST.get('state')
            obj.zipcode = request.POST.get('zipcode')
            obj.description = request.POST.get('description')
            obj.price = request.POST.get('price')
            obj.bedrooms = request.POST.get('bedrooms')
            obj.bathrooms = request.POST.get('bathrooms')
            obj.square_footage = request.POST.get('square_footage')
            obj.author = request.user
            for f in obj.images:
                file_instance = Listing(images=f)
                file_instance.save()
                print('images here')
            obj.save()
            print('obj saved')
            return redirect('/')
        else:
            form = ListingForm()
    context = {
        'form': form
    }

    return render(request, 'app/new_listing.html', context)

def edit_listing(request, id):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect("users:login")
    
    listing = get_object_or_404(Listing, id=id)

    if listing.author != user:
        return HttpResponse("You are not the author of this listing.")
    if request.POST:
        form = UpdateListingForm(request.POST or None, request.FILES or None, instance=listing)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Listing Updated"
            listing = obj
            return redirect('detail')

    form = UpdateListingForm(instance=listing
        # initial={
        #     "title": listing.title,
        #     "body": listing.body,
        #     "image": listing.image,
        # }
    )
    context['form'] = form
    return render(request, 'app/edit_listing.html', context)