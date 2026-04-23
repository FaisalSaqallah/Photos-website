from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Submission

def upload_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        height_cm = request.POST.get('height_cm')
        front_photo = request.FILES.get('front_photo')
        side_photo = request.FILES.get('side_photo')
        terms_agreed = request.POST.get('terms_agreed')

        if name and height_cm and front_photo and side_photo and terms_agreed:
            Submission.objects.create(
                name=name,
                height_cm=height_cm,
                front_photo=front_photo,
                side_photo=side_photo
            )
            messages.success(request, 'Successfully uploaded data! Thank you.')
            return redirect('upload')
        else:
            messages.error(request, 'Please provide all fields and agree to the terms.')
            
    return render(request, 'index.html')
