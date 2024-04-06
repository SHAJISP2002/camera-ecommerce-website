from django.urls import path
from . import views
from .views import place_order

urlpatterns=[
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('collections',views.collections,name="collections"),
    path('collections/<slug:name>/', views.collections_view, name='catagory_collections'),
    path('product/<int:product_id>/', views.product_detail_view, name='product_detail_view'),
    path('thank_you', views.thanks_you_page, name='thanks_you_page'),
    path('place_order/', views.place_order, name='place_order'),
    path('aboutas/', views.about, name='aboutas'),
     
    
    ]