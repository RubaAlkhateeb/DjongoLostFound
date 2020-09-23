from django.urls import path
#from . import views
from .views import IndexView, AddView, ItemView

urlpatterns = [
    # path('', views.index, name='index'),
    # path('Add/', views.Add, name='Add'),
    path('', IndexView.as_view(), name="index"),
    path('Add/', AddView.as_view(), name='Add'),
    path('viewitem/<int:pk>', ItemView.as_view(), name='viewitem'),
]