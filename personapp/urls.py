from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('persons/', views.PersonList.as_view(), name='person-list'),
    path('person/<int:pk>/', views.PersonDetail.as_view(), name='person-detail'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)