from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('tags/', views.TagsList.as_view()),
    path('tags/<str:tags>/', views.UsersList.as_view()),
    path('users_list/', views.UsersList.as_view()),
    path('user_tag/', views.UserTag.as_view()),
    path('user_tag/<int:pk>/', views.UserTag.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
