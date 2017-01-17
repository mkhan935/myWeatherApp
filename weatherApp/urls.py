
from django.conf.urls import url
from django.contrib import admin
import station.views

urlpatterns = [
    url(r'^home$', station.views.homePage,name="homePage"),
    url(r'^$',station.views.getZipCode,name="getZIP")
]
