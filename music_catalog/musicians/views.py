from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet

from .models import Album, Musician, Song, SongAlbum
from .serializers import (
    AlbumSerializer,
    MusicianSerializer,
    SongAlbumSerializer,
    SongSerializer,
)


class MusicianViewSet(ModelViewSet):
    queryset = Musician.objects.all().order_by("name")
    serializer_class = MusicianSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all().order_by("musician__name", "year")
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all().order_by("name")
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SongAlbumViewSet(ModelViewSet):
    queryset = SongAlbum.objects.all().order_by("album__name", "number")
    serializer_class = SongAlbumSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
