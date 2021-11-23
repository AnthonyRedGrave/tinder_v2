from django.db import models
from profiles.models import Profile
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

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


@receiver(post_save, sender=Profile)
def _post_save_profile(sender, instance, *args, **kwargs):
    Gallery.objects.create(profile = instance)

