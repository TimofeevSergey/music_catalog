from rest_framework.serializers import ModelSerializer

from .models import Album, Musician, Song, SongAlbum


class MusicianSerializer(ModelSerializer):
    class Meta:
        model = Musician
        fields = ["id", "name"]


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = ["id", "musician", "year"]


class SongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "name"]


class SongAlbumSerializer(ModelSerializer):
    class Meta:
        model = SongAlbum
        fields = ["album", "number", "song"]
