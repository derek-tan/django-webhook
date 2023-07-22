from django.urls import path

from webhook import views

urlpatterns = [
    path("", views.index, name="index"),
    path("soda/agreement", views.subscribe_soda_agreement, name="soda_agreement"),
    path("soda/notification", views.subscribe_soda_notification, name="soda_notification"),
    path("soda/incident", views.subscribe_soda_incident, name="soda_incident"),
]
