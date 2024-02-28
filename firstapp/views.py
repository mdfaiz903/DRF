from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET','POST'])

def firstapi(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        print(name,age)
        return Response(
            {'name':name,'age':age}
        )
    else:

        context={
            'name':'md faiz',
            'UV':'NORTHERN UNIVERSITY BANGLADESH'


        }
    return Response(context)


