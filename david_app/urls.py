from django.urls import path
from david_app import views

# The app name and the name variable together uniquely identify the views to point to
# They are used in the project html templates/they should be used in the hubapp html templates, which may need updating

app_name = "david_app"

urlpatterns = [
    path("", views.david_app, name='david_app'),
    path('david_app', views.david_app, name='david_app'),
]