from django.urls import path, include

from products import views

urlpatterns = [
    path('lastest-products/', views.LatestProductList.as_view()),
    
]