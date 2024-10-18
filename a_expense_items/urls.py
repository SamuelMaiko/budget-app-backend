from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyExpenseItemsView.as_view(), name='expense-items'),
    path('create/', views.CreateExpenseItemsView.as_view(), name='create-expense-item'),
    path('create-and-add/', views.CreateAndAddItemToWeekView.as_view(), name='create-and-add-to-week'),
]

# create an item - using just the name
# add an item to a week
# remove the item from the week
# list of the items for the user along with if in the week or not 
# edit the week expense item - amount_allocated and name
# change the money values
