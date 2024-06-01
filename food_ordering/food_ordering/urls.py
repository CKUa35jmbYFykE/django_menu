# food_ordering/urls.py
from django.contrib import admin
from django.urls import path
from menu import views
from django.conf.urls.static import static
from django.conf import settings
from menu.views import order_confirmation, register_view, logout_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dish_list, name='dish_list'),
    path('order/<int:dish_id>/', views.order_dish, name='order_dish'),
    path('admin/add-dish/', views.admin_add_dish, name='admin_add_dish'),
    path('admin/orders/', views.admin_order_list, name='admin_order_list'),
    path('order-confirmation/', order_confirmation, name='order_confirmation'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'), 
    path('logout/', logout_view, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)