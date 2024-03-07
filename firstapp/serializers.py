from django import forms 
from . models import Contact,BlogPost
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


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        # fields=('user', 'title', 'details', 'created_at', 'is_active', )
        # fields='__all__'
        exclude = ['user','is_active']
class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields='__all__'
