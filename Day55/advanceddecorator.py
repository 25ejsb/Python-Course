class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def isAuthenticatedDecorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@isAuthenticatedDecorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post")

new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)