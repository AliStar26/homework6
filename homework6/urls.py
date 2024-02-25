
from django.contrib import admin
from django.urls import path
from app.views import home,about


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name= 'home'),
    path('about/<int:kiosk_id>', about,name='about'),


]
