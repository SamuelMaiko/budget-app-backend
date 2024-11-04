from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyWeeksView.as_view(), name='my-weeks'),
    path('<int:week_id>/', views.WeekDetailView.as_view(), name='week-detail'),
    path('create/', views.CreateWeeksView.as_view(), name='create-week'),
    path('<int:week_id>/delete/', views.DeleteWeekView.as_view(), name='delete-week'),
    path('<int:week_id>/add-item/', views.AddItemView.as_view(), name='add-expense-item'),
    path('<int:week_id>/remove-item/', views.RemoveItemView.as_view(), name='remove-expense-item'),
    path('edit-week-item/<int:week_item_id>/', views.EditWeekItemView.as_view(), name='edit-week-item'),
    path('week-item/<int:week_item_id>/withdraw/', views.WithdrawWeekItemView.as_view(), name='withdraw-week-item'),
    path('<int:week_id>/statements/', views.WeekStatementsView.as_view(), name='week-statements'),
]
