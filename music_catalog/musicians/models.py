from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

YEAR_MIN_VALUE = 1917
YEAR_MAX_VALUE = 2100


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Musician(BaseModel):
    name = models.CharField(max_length=40, verbose_name="Название", unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Исполнители"
        verbose_name = "Исполнитель"
        ordering = ["name"]


class Album(BaseModel):
    musician = models.ForeignKey(Musician, on_delete=models.PROTECT, verbose_name="Исполнитель")
    year = models.PositiveSmallIntegerField(
        verbose_name="Год", validators=[MinValueValidator(YEAR_MIN_VALUE), MaxValueValidator(YEAR_MAX_VALUE)]
    )

    def __str__(self):
        return str(self.musician) + " (" + str(self.year) + ")"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["musician", "year"],
                name="%(app_label)s_%(class)s_unique_musician_year",
            ),
        ]
        verbose_name_plural = "Альбомы"
        verbose_name = "Альбомы"
        ordering = ["musician", "year"]


class Song(BaseModel):
    name = models.CharField(max_length=100, verbose_name="Название")
    albums = models.ManyToManyField(Album, verbose_name="Альбомы песни", through="SongAlbum")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Песни"
        verbose_name = "Песня"
        ordering = ["name"]


class SongAlbum(BaseModel):
    song = models.ForeignKey(Song, on_delete=models.PROTECT, verbose_name="Песня")
    album = models.ForeignKey(Album, on_delete=models.PROTECT, verbose_name="Альбом")
    number = models.PositiveSmallIntegerField(
        verbose_name="Порядковый номер", validators=[MinValueValidator(1), MaxValueValidator(99)]
    )

    def __str__(self):
        return str(self.album) + " - " + str(self.number) + ". " + str(self.song)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["album", "number"],
                name="%(app_label)s_%(class)s_unique_album_number",
            ),
            models.UniqueConstraint(
                fields=["album", "song"],
                name="%(app_label)s_%(class)s_unique_album_song",
            ),
        ]
        verbose_name_plural = "Песни в альбомах"
        verbose_name = "Песня в альбоме"
        ordering = ["album", "number"]
