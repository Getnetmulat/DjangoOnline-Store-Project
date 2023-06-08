from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, redirect
from Account.models import User, Address
from .models import *
# Create your views here.
def contact(request):
    if request.method=="POST":       
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        alert = True
        return render(request, 'contact.html', {'alert':alert})
    return render(request, "contact.html")
# Insert data (Create a new user with an address)
def create_user(request):
    if request.method == 'POST':
    # Retrieve the form data
        username = request.POST['username']
        email = request.POST['email']
        street_address = request.POST['street_address']
        city = request.POST['city']
        state = request.POST['state']
        postal_code = request.POST['postal_code']
        country = request.POST['country']
        # Create the address instance
        address = Address.objects.create(street_address=street_address, city=city,
        state=state, postal_code=postal_code, country=country)
        # Create the user instance with the associated address
        user = User.objects.create(username=username, email=email, address=address)
        # Redirect to a success page or perform other actions
        return redirect('success_page')
    return render(request, 'create_user.html')

# Update data (Modify user and address information)
def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    address = user.address
    if request.method == 'POST':
# Retrieve the form data
        email = request.POST['email']
        city = request.POST['city']
        state = request.POST['state']
        postal_code = request.POST['postal_code']
        # Update the user and address fields
        user.email = email
        address.city = city
        address.state = state
        address.postal_code = postal_code
        # Save the updated user and address
        user.save()
        address.save()
        # Redirect to a success page or perform other actions
        return redirect('success_page')
    return render(request, 'update_user.html', {'user': user, 'address': address})
#Delete data (Remove a user and their address)
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    address = user.address
    if request.method == 'POST':
        # Delete the user and address objects
        user.delete()
        address.delete()
        # Redirect to a success page or perform other actions
        return redirect('success_page')
    return render(request, 'delete_user.html', {'user': user, 'address': address})
# Select data (Retrieve user and address information)
def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    address = user.address
    return render(request, 'user_detail.html', {'user': user, 'address': address})


def index(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'], password=request.POST['password'],  firstname=request.POST['firstname'], lastname=request.POST['lastname'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'web/index.html')

def login(request):
    return render(request, 'web/login.html')

def home(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'web/home.html', {'member': member})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'web/login.html', context)

