from django.apps import AppConfig

# Define a configuration class for the Django app named 'generator'
class GeneratorConfig(AppConfig):
    # Specify the default auto-generated primary key field for models in this app
    default_auto_field = "django.db.models.BigAutoField"
    
    # Set the name of the app
    name = "generator"

