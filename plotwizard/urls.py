from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('datalines/', views.DataLineListView.as_view(), name='datalines'),
    path('listapp/', include('listapp.urls'))
]