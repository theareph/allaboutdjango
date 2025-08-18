from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

book_router = DefaultRouter()
book_router.register("", views.BookViewSet, "book")

app_name = "core"
api_urlpatterns = [
    path("weather/", views.WeatherAPIView.as_view(), name="weather"),
    path("server-distro/", views.ServerDistroAPIView.as_view(), name="server-distro"),
    path("devlogs/", views.DevlogListAPIView.as_view(), name="devlogs"),
    path("visits/", views.VisitsAPIView.as_view(), name="visits"),
    path("books/", include(book_router.urls)),
]

urlpatterns = [
    path("redir/<str:to_alias>/", views.simple_redirect, name="simple_redirect"),
    path("api/", include(api_urlpatterns)),
]
