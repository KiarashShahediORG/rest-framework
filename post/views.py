from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from .permissions import IsAuthorOrReadonly

# Create your views here.

class PostList(generics.ListCreateAPIView):

    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    






class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthorOrReadonly,) 
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
 