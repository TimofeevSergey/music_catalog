from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from .views import AlbumViewSet, MusicianViewSet, SongAlbumViewSet, SongViewSet

router = DefaultRouter()
router.register(r"musicians", MusicianViewSet)
router.register(r"albums", AlbumViewSet)
router.register(r"song", SongViewSet)
router.register(r"songalbums", SongAlbumViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api/", include("rest_framework.urls", namespace="rest_framework")),
    path(
        "openapi/",
        get_schema_view(title="Musicians", description="API for all Musicians", version="1.0.0"),
        name="openapi-schema",
    ),
    path(
        "swagger-ui/",
        TemplateView.as_view(template_name="swagger-ui.html", extra_context={"schema_url": "openapi-schema"}),
        name="swagger-ui",
    ),
]
