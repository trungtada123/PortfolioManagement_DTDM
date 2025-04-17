from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . import views_wallet
import portfolio.views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('portfolios/', views.portfolio_list, name='portfolio_list'),
    path('portfolios/create/', views.portfolio_create, name='portfolio_create'),
    path('portfolios/<int:pk>/', views.portfolio_detail, name='portfolio_detail'),
    path('portfolios/<int:pk>/update/', views.portfolio_update, name='portfolio_update'),
    path('portfolios/<int:portfolio_id>/buy/', views.buy_stock, name='buy_stock'),
    path('portfolios/<int:portfolio_id>/sell/', views.sell_stock, name='sell_stock'),
    path('portfolios/<int:portfolio_id>/transactions/', views.portfolio_transactions, name='portfolio_transactions'),
    
    path('assets/', views.asset_list, name='asset_list'),
    path('assets/create/', views.asset_create, name='asset_create'),
    path('assets/<int:pk>/', views.asset_detail, name='asset_detail'),
    path('assets/<int:pk>/update/', views.asset_update, name='asset_update'),
    
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transactions/create/', views.transaction_create, name='transaction_create'),
    
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='portfolio/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('market/', views.market, name='market'),
    path('api/historical-data/<str:symbol>/', views.get_stock_historical_data, name='get_stock_historical_data'),
    
    # URLs cho ví điện tử
    path('wallet/', views_wallet.wallet, name='wallet'),
    path('wallet/deposit/', views_wallet.deposit_money, name='deposit_money'),
    path('wallet/withdraw/', views_wallet.withdraw_money, name='withdraw_money'),
    path('wallet/transactions/', views_wallet.wallet_transactions, name='wallet_transactions'),
    path('wallet/bank-accounts/', views_wallet.bank_account_list, name='bank_account_list'),
    path('wallet/bank-accounts/create/', views_wallet.bank_account_create, name='bank_account_create'),
    path('wallet/bank-accounts/<int:pk>/update/', views_wallet.update_bank_account, name='bank_account_update'),
    path('wallet/bank-accounts/<int:pk>/delete/', views_wallet.delete_bank_account, name='bank_account_delete'),
    path('wallet/bank-accounts/<int:pk>/set-default/', views_wallet.set_default_bank_account, name='bank_account_set_default'),
    
    # API URLs
    path('api/historical-data/<str:symbol>/', views.get_historical_data_api, name='historical_data_api'),
    path('api/ai-chat/', views.ai_chat_api, name='ai_chat_api'),
    # ===== FCM token view =====
    path('save-fcm-token/', views.save_fcm_token, name='save_fcm_token'),
]