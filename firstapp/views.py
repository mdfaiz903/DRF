from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated,AllowAny
from . models import Contact,BlogPost
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,ListAPIView,ListCreateAPIView,RetrieveAPIView

from .serializers import ContactSerializer,PostSerializer,PostDetailSerializer
# Create your views here.



@api_view(['POST',])
def registraionAPI(request):
    if request.method=='POST':
        username=request.data['username']
        email=request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        password1=request.data['password1']
        password2=request.data['password2']

        if User.objects.filter(username=username).exists():
            return Response({"error":"User already Exists!"})
        elif password1!=password2:
            return Response({"error":"Two password didn't matched"})
        
        else:
            user = User()
            user.username = username
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.is_active = True
            user.set_password(raw_password=password1)
            user.save()
            return Response({"Success":"user successfully registered!"})
        
        




@api_view(['GET','POST'])
@permission_classes([IsAuthenticated,])
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


# @api_view(['POST',])
class ContactapiView(APIView):
    permission_classes=[AllowAny,]
    def post(self,request,format=None):
        data = request.data
        serializer = ContactSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,{"success":"Successfully saved!"})

        
        # return Response()
    def get(self,request,format=None):
        # queryset = Contact.objects.all()
        queryset = Contact.objects.get(id=2)
        # serializer = ContactSerializer(queryset, many=True) #For all data
        serializer = ContactSerializer(queryset, many=False) #For single data
        return Response(serializer.data)
        


from rest_framework import status 
# class PostCreateApiView(CreateAPIView):
#     permission_classes = [IsAuthenticated,]
#     queryset = BlogPost.objects.all()
#     serializer_class = PostSerializer

#     def perform_create(self, serializer):
#         return serializer.save(user = self.request.user)


#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         instance = self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)


#         seria = PostDetailSerializer(instance=instance, many=False)
        
#         return Response(seria.data, status=status.HTTP_201_CREATED, headers=headers)
    



# class PostListApiView(ListAPIView):
#     permission_classes = [IsAuthenticated,]
#     queryset = BlogPost.objects.all()
#     serializer_class= PostDetailSerializer

        
class PostCreateApiView(ListCreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)


        seria = PostDetailSerializer(instance=instance, many=False)
        
        return Response(seria.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PostDetailSerializer(queryset, many=True)
        return Response(serializer.data)
    
    #get_queryset customization
    def get_queryset(self):
        queryset = BlogPost.objects.filter(is_active=True)
        return queryset





class PostRetriveAPIVIEW(RetrieveAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = BlogPost.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field='id'

