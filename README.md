# hello-graphene

Clone the repo first.

Install the Python runtime then follow this guideline for the detail explanation:

https://sourabhbajaj.com/mac-setup/Python/virtualenv.html

Then follow these instructions below:

```
$ cd hello-graphene
$ virtualenv hello-graphene-env
$ source hello-graphene-env/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver 0.0.0.0:8080
```

Then access this URL to open the GraphiQL: http://localhost:8080/blog-relay.

You can check the sample GraphQL query within `<root>/hello_graphql/schema.py`