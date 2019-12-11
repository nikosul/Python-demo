from django.urls import path
from . import views

# urls
app_name = 'demoapp'
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:book_id>/', views.details, name='details')
]