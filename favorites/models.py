from django.db import models

class Favorites(models.Model):
    title = models.CharField("Название тега", max_length=60)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
