from django.urls import path, include
from rest_framework.routers import DefaultRouter

from snippets import views

# Short answer: with DefaultRouter you don’t need your own api_root — the router auto-generates an API root view for /
# that lists your registered routes. In your snippet, your custom api_root() function
# isn’t used at all because your urlpatterns only include router.urls.
#
# Here’s what’s happening and your options:
#
# What DefaultRouter does
# When you do:
# router = DefaultRouter()
# router.register(r'snippets', SnippetViewSet, basename='snippet')
# router.register(r'users', UserViewSet, basename='user')
# urlpatterns = [ path('', include(router.urls)), ]
#
# DefaultRouter creates:
# an API root at / (class: APIRootView)
# named routes like:
# snippet-list, snippet-detail
# user-list, user-detail
# So visiting / returns something like:
# {
#   "snippets": "http://.../snippets/",
#   "users": "http://.../users/"
# }


# Using ViewSets can be a really useful abstraction. It helps ensure that URL conventions will be consistent across
# your API, minimizes the amount of code you need to write, and allows you to concentrate on the interactions and
# representations your API provides rather than the specifics of the URL conf.
# That doesn't mean it's always the right approach to take. There's a similar set of trade-offs to consider
# as when using class-based views instead of function-based views.
# Using ViewSets is less explicit than building your API views individually.

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
