import graphene

import blog.schema
import blog.relay
from blog.mutations import CategoryMutation, DeleteCategoryMutation, BlogPostMutation, DeleteBlogPostMutation


class BlogQuery(blog.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


blog_schema = graphene.Schema(query=BlogQuery)


class BlogQueryRelay(blog.relay.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class BlogQueryRelayMutation(graphene.ObjectType):
    """
    - example mutation for create operation:
    
    mutation:

    ```
    mutation ($input: CategoryMutationInput!) {
      createOrUpdateCategory(input: $input) {
          name
      }
    }
    ```
    
    input: 

    ```
    {
      "input":  {
        "name": "Neural Network"
      }
    }
    ```

    - example mutation for update operation:

    mutation:

    ```
    mutation  {
      createOrUpdateCategory( input: {id: 5, name: "Neural NETWORK!"}) {
            name
      }
    }
    ``` 

    - exapmle mutation for delete operation:

    ```
    mutation  {
      deleteCategory( input: { id:48 }) {
        category {
          id
        }
      }
    }
    ```
    
    - example mutation for create blogpost:

    ```
    mutation  {
      createOrUpdateBlogPost(input: {
          title: "lorem ipsum 3", 
          body: "hello world man!", 
          category: "41"
      }) {
          title
      }
    }
    ```

    - example mutation for update blogpost:

    ```
    mutation  {
      createOrUpdateBlogPost(input: {
          id: 3,
          title: "lorem ipsum 333333", 
          body: "hello world man!", 
          category: "41"
      }) {
          title
      }
    }
    ```

    - example mutation for delete blogpost:
    ```
    mutation  {
      deleteBlogPost(input: { id: 3}){
          blogPost{
            id
            title
          }
      }
    }
    ```
    """

    createOrUpdateCategory = CategoryMutation.Field()
    deleteCategory = DeleteCategoryMutation.Field()
    createOrUpdateBlogPost = BlogPostMutation.Field()
    deleteBlogPost = DeleteBlogPostMutation.Field()


blog_schema_relay = graphene.Schema(query=BlogQueryRelay, mutation=BlogQueryRelayMutation)