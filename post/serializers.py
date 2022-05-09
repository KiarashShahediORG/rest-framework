from rest_framework import serializers
from .models import Post



class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post 
        fields = ('id', 'author', 'title', 'body', 'created_at') #neshon dadan in bakhsh haye model b sorat jason be karbar
          