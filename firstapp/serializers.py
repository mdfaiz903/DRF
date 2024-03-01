from django import forms 
from . models import Contact
from rest_framework import serializers
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        # fields = ['name','email','phone','subject','details']
        fields = '__all__'
