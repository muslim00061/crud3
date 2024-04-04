from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('board/add/', views.add_board_page, name='add_board_page'),
    path('board/detail/<int:pk>/', views.board_detail_page, name='board_detail_page'),
    path('board/delete/<int:pk>/', views.delete_board_page, name='delete_board_page'),
    path('board/edit/<int:pk>/', views.edit_board_page, name='edit_board_page'),
]