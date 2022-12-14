"""volento URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from event import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/eventcategory', views.EventCategoryList.as_view()),
    path('api/eventsponser', views.EventSponserList.as_view()),
    path('api/event', views.EventList.as_view()),
    path('api/eventimage', views.EventImageList.as_view()),
    path('api/eventagenda', views.EventAgendaList.as_view()),
    path('api/eventmember', views.EventMemberList.as_view()),
    path('api/eventwishlist', views.EventUserWishListList.as_view()),
    path('api/usercoin', views.UserCoinList.as_view()),
]
