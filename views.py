from django.shortcuts import render
from .models import ConfigSettings
from .forms import ConfigForm

def config_settings(request):
    # Retrieve all configuration settings
    configs = ConfigSettings.objects.all()
    
    # If the form is submitted (POST request), process the form
    if request.method == "POST":
        form = ConfigForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new or updated setting
    else:
        form = ConfigForm()  # Display an empty form for GET requests
    
    # Render the config template with the form and current settings
    return render(request, "dashboard/config.html", {"form": form, "configs": configs})
