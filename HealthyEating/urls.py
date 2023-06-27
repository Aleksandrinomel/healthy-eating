"""
URL configuration for HealthyEating project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from healthapp.views import index_page, RegisterUser, LoginUser, logout_user, index_page3
from healthapp.views import profile
from healthapp.views import buttons
from healthapp.views import cards
from healthapp.views import charts
from healthapp.views import forgot_password
# from healthapp.views import login
# from healthapp.views import register
from healthapp.views import tables
from healthapp.views import products
from healthapp.views import utilities_animation
from healthapp.views import utilities_border
from healthapp.views import blank
from healthapp.views import utilities_color
from healthapp.views import utilities_other

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='index'),
    path('ind', index_page3, name='index3'),
    path('profile', profile, name='profile'),
    path('blank.html', blank),
    path('buttons.html', buttons),
    path('cards.html/', cards),
    path('charts.html/', charts),
    path('forgot-password.html/', forgot_password),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('tables.html/', tables),
    path('products.html/', products),
    path('utilities-animation.html/', utilities_animation),
    path('utilities-border.html/', utilities_border),
    path('utilities-color.html/', utilities_color),
    path('utilities-other.html/', utilities_other),
]
