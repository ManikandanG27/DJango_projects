from django.apps import AppConfig

# Define a custom configuration for your Django app
class MyappConfig(AppConfig):
    # Specify the default auto field to use for models in this app
    default_auto_field = "django.db.models.BigAutoField"
    
    # Set the name of the app
    name = "myapp"
