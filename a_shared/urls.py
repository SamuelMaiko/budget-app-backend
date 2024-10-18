from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('auth/', include("a_authentication.urls")),
    path('profile/', include("a_profile.urls")),
    path('wallets/', include("a_wallet.urls")),
    path('weeks/', include("a_weekly_budget.urls")),
    path('expense-items/', include("a_expense_items.urls")),
]
