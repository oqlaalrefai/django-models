from django.urls import path
from .views import snackList,snackDetail
urlpatterns = [
    path('',snackList.as_view(),name='snack_list'),
    path('<int:pk>',snackDetail.as_view(),name='snack_detail')
]