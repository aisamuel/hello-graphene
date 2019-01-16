from rest_framework import serializers
from .models import Category, BlogPost


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')
        read_only_fields = ()


class BlogPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'body', 'category')
        read_only_fields = ()
