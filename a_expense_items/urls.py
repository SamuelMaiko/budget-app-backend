from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyExpenseItemsView.as_view(), name='expense-items'),
    path('', views.MyExpenseItemsView.as_view(), name='expense-items'),
    path('create/', views.CreateExpenseItemsView.as_view(), name='create-expense-item'),
]
