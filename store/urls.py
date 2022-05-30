from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.designstore, name="designstore"),
    path('designstore2/', views.designstore2, name="designstore2"),
    path('login/', views.sitelogin, name="login"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.cart, name="checkout"),
    path('viewitem/', views.viewitem, name="viewitem"),
    #path('form_page/', views.cart, name="formpage"),
    path('formpage/', views.form_name_view, name="form_name"),
	
]