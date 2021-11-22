from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    class StatusChoices(models.TextChoices):
        default = "default", "Обычный"
        premium = "premium", "Премиум"
        vip = "vip", "Вип"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField("Статус профиля", choices=StatusChoices.choices, max_length=15)
    # information = models.OneToOneField('ProfileInformation', on_delete=models.CASCADE, related_name='profile')

    def __str__(self) -> str:
        return f"Профиль пользователя {self.user.username}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Photo(models.Model):
    image = models.ImageField("Изображения для профиля", )
    gallery = models.ForeignKey('Gallery', on_delete=models.CASCADE, related_name='photos')

    def __str__(self) -> str:
        return self.image.name

    class Meta:
        verbose_name = "Изображение для профиля"
        verbose_name_plural = "Изображения для профиля"
    
class Gallery(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='gallery')
    
    def __str__(self) -> str:
        return f"Галерея изображения профиля {self.profile.user.username}"

    class Meta:
        verbose_name = "Галерея профилей"
        verbose_name_plural = "Галереи профилей"