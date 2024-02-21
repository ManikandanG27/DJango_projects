# Import necessary functions and modules
from django.shortcuts import render
from django.http import HttpResponse

# View function for rendering the index page
def index(request):
    return render(request, 'myapp/index.html')

# View function for handling form submission and rendering the greet page
def greet(request):
    if request.method == 'POST':  # Check if the request method is POST
        name = request.POST.get('name', '')  # Get the value of 'name' from the POST data
        if name:  # If 'name' is provided
            # Render the greet page and pass the name as context data
            return render(request, 'myapp/greet.html', {'name': name})
        else:  # If 'name' is not provided
            # Render the index page with an error message
            return render(request, 'myapp/index.html', {'error_message': 'Please provide your name.'})
    else:  # If the request method is not POST
        return HttpResponse('Method not allowed')  # Return a response indicating that the method is not allowed
