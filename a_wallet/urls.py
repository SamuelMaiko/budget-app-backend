from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyWalletsView.as_view(), name='my-wallets'),
    path('<int:wallet_id>/', views.WalletDetailView.as_view(), name='wallet-detail'),
    path('transfer-funds/', views.TransferWalletFundsView.as_view(), name='transfer-wallet-funds'),
    path('create/', views.CreateWalletView.as_view(), name='create-wallet'),
    path('<int:wallet_id>/edit/', views.EditWalletView.as_view(), name='edit-wallet'),
    path('<int:wallet_id>/delete/', views.DeleteWalletView.as_view(), name='delete-wallet'),
    path('<int:wallet_id>/deposit-funds/', views.DepositFundsView.as_view(), name='deposit-funds'),
    path('<int:wallet_id>/transactions/', views.WalletTransactionsView.as_view(), name='wallet-transactions'),
]
 