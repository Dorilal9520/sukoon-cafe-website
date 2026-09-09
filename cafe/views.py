from django.shortcuts import render, redirect
from django.contrib import messages
from .models import contactMessage
from django.urls import reverse

# Create your views here.

def contact_view(request):
    if request.method == "POST":
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        email = request.POST.get("email")
        message = request.POST.get("message")


        contactMessage.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            message=message
        )

        messages.success(request, "Thanks you! Your message has been sent successfully.")
        return redirect("home") 

    return render(request, "index.html")
    