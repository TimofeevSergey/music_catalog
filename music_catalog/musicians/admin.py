from django.contrib import admin

from .models import Album, Musician, Song, SongAlbum


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    search_fields = ("name",)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("musician", "year")
    list_display_links = ("musician", "year")
    search_fields = ("musician", "year")


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    search_fields = ("name",)


@admin.register(SongAlbum)
class SongAlbumAdmin(admin.ModelAdmin):
    list_display = ("album", "number", "song")
    list_display_links = ("song",)
    search_fields = ("album", "number", "song")
