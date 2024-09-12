from django.urls import path 
from . import views

app_name = 'thoughts'

urlpatterns = [
    path('', views.Thoughts.as_view(), name="thoughts"),
    path('write', views.Write.as_view(), name="write"),
    path('library', views.Library.as_view(), name="library"),
    path('categories', views.Categories.as_view(), name="categories"),
    path('archived', views.Archived.as_view(), name="archived")
]
