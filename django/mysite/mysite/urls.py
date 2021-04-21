
from django.contrib import admin
from django.urls import path

app_name = "main"  

urlpatterns = [
    path('admin/', admin.site.urls),
        path("", views.homepage, name="homepage"),

    path("register", views.register_request, name="register")
]
