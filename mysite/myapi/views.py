# views.py
from rest_framework import viewsets

from .serializers import WishlistsSerializer
from .models import Wishlists

from .serializers import AddressesSerializer
from .models import Addresses

from .serializers import AuthorsSerializer
from .models import Authors

from django.db import IntegrityError # Import IntegrityError
from rest_framework.exceptions import APIException  #Import APIException
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
            
class WishlistsViewSet(viewsets.ModelViewSet):
    queryset = Wishlists.objects.all().order_by('id')
    serializer_class = WishlistsSerializer          
    def list(self, request):
        queryset = Wishlists.objects.all().order_by('id')
        userid = self.request.query_params.get('userid')
        name = self.request.query_params.get('name')
        if userid and name:
            queryset = queryset.filter(userid=userid)
            queryset = queryset.filter(name=name)
            books = queryset.values('bookid', 'bookid__name')
            return Response({"Books": list(books)})
        queryset = queryset.values('id', 'userid', 'userid__firstname', 'bookid', 'bookid__name', 'name')
        return Response({"Wishlist Results": list(queryset)})        
    def delete(self, request, pk):
        instance = Wishlists.objects.get(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as exc:
            raise APIException("Cannot insert a book twice into the same wishlist")
            
class AddressesViewSet(viewsets.ModelViewSet):
    queryset = Addresses.objects.all().order_by('id')
    serializer_class = AddressesSerializer

class AuthorsViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all().order_by('id')
    serializer_class = AuthorsSerializer
            
class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all().order_by('name')
    serializer_class = BooksSerializer
    
class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all().order_by('genre')
    serializer_class = GenresSerializer
            

