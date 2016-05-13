from django.shortcuts import render
from rest_framework import generics
from .serializers import CategoriaSerializer,PessoaSerializer,UserSerializer,FerramentaSerializer
from .models import Categoria,Pessoa,Ferramenta
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate

class CategoriaList(generics.ListCreateAPIView):    
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(),)   

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class FerramentaList(generics.ListCreateAPIView):    
    queryset = Ferramenta.objects.all()
    serializer_class = FerramentaSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(),)   

class FerramentaDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Ferramenta.objects.all()
    serializer_class = FerramentaSerializer

class PessoaList(generics.ListCreateAPIView):    
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer        
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(),)     


class PessoaDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer  

class UserList(generics.ListCreateAPIView):    
    queryset = User.objects.all()
    serializer_class = UserSerializer    
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(),)     


class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer  
