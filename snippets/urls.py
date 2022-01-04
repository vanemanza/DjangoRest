from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('', views.api_root),
    #path('snippets/', views.snippet_list),
    #path('snippets/<int:pk>/', views.snippet_detail),
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

"""
add support for format suffixes to our API endpoints.
Using format suffixes gives us URLs that explicitly refer to a given 
format, and means our API will be able to handle URLs such as 
http://example.com/api/items/4.json.
"""
