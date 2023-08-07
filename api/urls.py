from django.urls import path, include
from rest_framework.authtoken import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home_api'),
    path('category/', include('api.category.urls')),
    path('product/', include('api.product.urls')),
    path('user/', include('api.user.urls')),
    path('order/', include('api.order.urls')),
    path('payment/', include('api.payment.urls')),
    path('api-token-auth/', auth_views.obtain_auth_token, name='api_token_auth'),
    
]