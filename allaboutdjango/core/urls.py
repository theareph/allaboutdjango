from django.urls import include, path

from . import views

app_name = "core"
api_urlpatterns = [
    path("weather/", views.WeatherAPIView.as_view(), name="weather"),
]
urlpatterns = [path("api/", include(api_urlpatterns))]
