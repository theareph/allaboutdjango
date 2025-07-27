from django.urls import include, path

from . import views

app_name = "core"
api_urlpatterns = [
    path("weather/", views.WeatherAPIView.as_view(), name="weather"),
    path("server-distro/", views.ServerDistroAPIView.as_view(), name="server-distro"),
]

urlpatterns = [path("api/", include(api_urlpatterns))]
