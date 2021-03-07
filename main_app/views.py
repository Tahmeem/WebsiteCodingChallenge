from django.shortcuts import render
from .models import users
from django.forms import ModelForm
from django.db import models
from django import forms
#Needed libraries and classes are imported
class extraForm(forms.Form): #For the current name entry
    current_name=forms.CharField(max_length=100,required = False)

class detailsForm(ModelForm): #Main model which takes in name and image as fields
    class Meta:
        model = users #in models.py
        fields = ['Name', 'img']

def enter(request): #Is run when url calls it
    form = detailsForm(request.POST or None, request.FILES) #Taking form data
    second_Form=extraForm(request.POST or None)
    valid = request.POST.get('validation') #To determine which checkbox is clicked
    if valid == "New User" and form.is_valid():
        form.save() #Saves data for new user
    elif valid == "Pre-existing User" and second_Form.is_valid() and form.is_valid():
        current_name = second_Form.cleaned_data.get('current_name')
        New_Name=form.cleaned_data.get('Name')
        Image = form.cleaned_data['img']
        if New_Name and Image: #Updates both image and new name
            user = users.objects.filter(Name=current_name)
            user.update(Name=New_Name,img=Image) #Gets the relevent query and updates info
        elif New_Name: #Only update to new name
            users.objects.filter(Name=current_name).update(Name=New_Name)
        elif Image: #Only update to image
            users.objects.filter(Name=current_name).update(img=Image)


    context = { #To pass in both forms to html
        'form': form,
        'second_Form':second_Form
    }
    return render(request, 'main_app/home.html', context) #Renders the html

