from graphene_django.rest_framework.mutation import SerializerMutation
from graphene import relay
from .serializers import CategorySerializer, BlogPostSerializer
from .models import Category, BlogPost
from .relay import CategoryNode, BlogPostNode

import graphene


class CategoryMutation(SerializerMutation):

    class Meta:
        serializer_class = CategorySerializer
        model_operations = ['create', 'update']
        lookup_field = 'id'


class DeleteCategoryMutation(relay.ClientIDMutation):

    class Input:
        id = graphene.Int(required=True)

    category = graphene.Field(CategoryNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, client_mutation_id=None):
        category = Category.objects.get(pk=id)
        category.delete()

        return DeleteCategoryMutation(category=category)


class BlogPostMutation(SerializerMutation):

    class Meta:
        serializer_class = BlogPostSerializer
        model_operations = ['create', 'update']
        lookup_field = 'id'


class DeleteBlogPostMutation(relay.ClientIDMutation):

    class Input:
        id = graphene.Int(required=True)

    blog_post = graphene.Field(BlogPostNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, client_mutation_id=None):
        blog_post = BlogPost.objects.get(pk=id)
        blog_post.delete()

        return DeleteBlogPostMutation(blog_post=blog_post)
