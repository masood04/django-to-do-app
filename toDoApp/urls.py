from django.urls import path
from . import views


urlpatterns = [
    path('', views.ToDoListView.as_view(), name='index'),
    path('list/<int:list_id>/', views.ItemListView.as_view(), name='list'),
    path('list/<int:list_id>/item/add', views.ItemCreateView.as_view(), name='add-item'),
    path('list/add', views.ListCreateView.as_view(), name='add-list'),
    path('list/<int:pk>/edit', views.ListUpdateView.as_view(), name='edit-list'),
    path('list/<int:pk>/delete', views.ListDeleteView.as_view(), name='delete-list'),
    path('list/item/<int:pk>/edit', views.ItemUpdateView.as_view(), name='edit-item'),
    path('list/<int:list_id>/item/<int:pk>/delete', views.ItemDeleteView.as_view(), name='delete-item'),

]
