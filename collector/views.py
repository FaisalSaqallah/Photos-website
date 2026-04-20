from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Submission

def upload_view(request):
    if request.method == 'POST':
        height_cm = request.POST.get('height_cm')
        front_photo = request.FILES.get('front_photo')
        side_photo = request.FILES.get('side_photo')

        if height_cm and front_photo and side_photo:
            Submission.objects.create(
                height_cm=height_cm,
                front_photo=front_photo,
                side_photo=side_photo
            )
            messages.success(request, 'Successfully uploaded data! Thank you.')
            return redirect('upload')
        else:
            messages.error(request, 'Please provide all fields.')
            
    return render(request, 'index.html')
