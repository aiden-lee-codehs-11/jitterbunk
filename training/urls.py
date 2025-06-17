from django.urls import path


from . import views

app_name = 'training'

urlpatterns = [
    path('', views.ResourceView.as_view(), name="index"),
    path('<int:pk>/', views.UserView.as_view(), name='personal'),
    path('<str:team>/', views.TeamView.as_view(), name='team'),
    path('<int:user_id>/add/', views.add, name="add"),
]