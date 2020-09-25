from django.urls import path
#from . import views
from .views import IndexView, AddView, ItemView, ItemDetail, DeleteItem

urlpatterns = [
    # path('', views.index, name='index'),
    # path('Add/', views.Add, name='Add'),
    path('', IndexView.as_view(), name="index"),
    path('Add/', AddView.as_view(), name='Add'),
    path('viewitem/', ItemView.as_view(), name='viewitem'),
    path('ItemDetail/(?P<pk>[\w\d\-\_]+)/$', ItemDetail.as_view(), name='ItemDetail'),
    path('ItemDetail/(?P<pk>[\w\d\-\_]+)/$/DeleteItem', DeleteItem.as_view(), name='DeleteItem'),
]