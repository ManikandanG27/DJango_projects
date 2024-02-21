from django.shortcuts import render
import random

# Define the views for your Django app

# View for the home page
def home(request):
    # Render the index.html template
    return render(request, "generator/index.html")

# View for generating a password
def password(request):
    # Define the character set for generating the password
    characters = list("abcdefghijklmnopqurstuvwxyz")
    
    # Get the desired length of the password from the request
    length = int(request.GET.get("length"))
    
    # If the user wants to include uppercase letters
    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    
    # If the user wants to include numbers
    if request.GET.get("numbers"):
        characters.extend(list("1234567890"))
    
    # If the user wants to include special characters
    if request.GET.get("special_characters"):
        characters.extend(list("!@#$%^&*()-_+={}[]|\\:;\"'"))
    
    # Generate the password using the selected character set and length
    password = ""
    for x in range(length):
        password += random.choice(characters)
    
    # Render the password.html template with the generated password
    return render(request, "generator/password.html", {"password": password})
