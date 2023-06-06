from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def greet_new_user(request):
    return HttpResponse("Welcome! Thank you for joining our online store.")
def user_profile(request):
    return render(request, 'company/index.html')


def user_profile_enhanced(request):
    # Variable values for profile fields
    username = "JohnDoe"
    email = "johndoe@example.com"
    # Add more variable values for other fields as needed
    # Prepare the context with variable values
    context = {
        'username': username,
        'email': email,
        # Add more fields and values to the context as needed
        }
    # Render the template with the context
    return render(request, 'company/profile_enhanced.html', context)

