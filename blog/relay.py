import graphene

from graphene import relay, ObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from .models import Category, BlogPost


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name',]
        interfaces = (relay.Node,)


class BlogPostNode(DjangoObjectType):
    class Meta:
        model = BlogPost
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'body': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node,)
        

class Query(object):
    """
    - Example GraphQL for Category:
    
    ```
    query {
      allCategories {
        edges {
          node{
            id
            name
          }
        }
      }
    }
    ```

    ```
    query {
      category(id: "Q2F0ZWdvcnlOb2RlOjE="){
        name
      }
    }
    ```

    ```
    query {
      allCategories{
        edges{
          node {
            id
            name
            blogPost { 
                edges {
                node{
                  id
                  title
                  body
                }
              }
            }
          }
        }
      }
    }
    ```

    ```
    query {
      allCategories(name: "Programming",) {
        edges{
          node {
            id
            name
            blogPost { 
                edges {
                node{
                  id
                  title
                  body
                }
              }
            }
          }
        }
      }
    }
    ```

    - Example GraphQL for BlogPost:

    ```
    query {
      allBlogPosts {
        edges {
          node {
            id
            title
            body
          }
        }
      }
    }
    ```
    
    ```
    query {
      allBlogPosts(category_Name: "Programming") {
        edges {
          node {
            id
            title
          }
        }
      }
    }
    ```
    
    ```
    query {
      allBlogPosts(title_Icontains: "1") {
        edges {
          node {
            id
            title
          }
        }
      }
    }
    ```

    ```
    query {
      allBlogPosts(title_Istartswith: ":Lor") {
        edges {
          node {
            id
            title
          }
        }
      }
    }
    ```
    """

    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    blog_post = relay.Node.Field(BlogPostNode)
    all_blog_posts =  DjangoFilterConnectionField(BlogPostNode)


