import graphene

from graphene_django.types import DjangoObjectType
from .models import Category, BlogPost


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class BlogPostType(DjangoObjectType):
    class Meta:
        model = BlogPost


class Query(object):
    all_categories = graphene.List(CategoryType)

    category = graphene.Field(CategoryType,
                                id=graphene.Int(),
                                name=graphene.String())

    all_blog_posts = graphene.List(BlogPostType)

    blog_post = graphene.Field(BlogPostType,
                                id=graphene.Int(),
                                title=graphene.String())

    def resolve_all_categories(self, info, *args, **kwargs):
        return Category.objects.all()

    def resolve_all_blog_posts(self, info, *args, **kwargs):
        return BlogPost.objects.select_related('category').all()

    def resolve_category(self, info, *args, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Category.objects.get(pk=id)

        if name is not None:
            return Category.objcets.get(name=name)

        return None

    def resolve_blog_post(self, info, *args, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')

        if id is not None:
            return BlogPost.objects.get(pk=id)

        if title is not None:
            return BlogPost.objcets.get(title=title)

        return None
