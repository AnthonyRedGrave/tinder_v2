from django.db import models
from django.contrib.auth.models import User
from favorites.models import Favorites


class Profile(models.Model):

    class StatusChoices(models.TextChoices):
        default = "default", "Обычный"
        premium = "premium", "Премиум"
        vip = "vip", "Вип"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField("Статус профиля", choices=StatusChoices.choices, max_length=15)

    def __str__(self) -> str:
        return f"Профиль пользователя {self.user.username}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Language(models.Model):
    class LanguageChoices(models.TextChoices):
        russian = "russian", "Русский"
        english = "english", "Английский"
        belarussian = "belarussian", "Беларусский"
        francian = "francian", "Французский"
        italian = "italian", "Итальянский"
    
    title = models.CharField("Язык", max_length=15, choices=LanguageChoices.choices)
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = "Языки"


class ProfileInformation(models.Model):

    class GenderChoices(models.TextChoices):
        male = "male", "Мужской"
        female = "female", "Женский"

    class EducationChoices(models.TextChoices):
        higher = "higher", "Высшее"
        secondary = "secondary", "Среднее"
        school = "school", "Школьное"

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='profile_information')
    gender = models.CharField("Пол", choices=GenderChoices.choices, max_length=20)
    languages = models.ManyToManyField(Language, verbose_name="Языки")
    education = models.CharField("Образование", choices=EducationChoices.choices, max_length=30)
    weight = models.DecimalField("Вес", decimal_places=1, max_digits=4, default=0)
    description = models.TextField("Описание профиля")
    location = models.CharField("Место расположения", max_length=150)
    favorites = models.ManyToManyField(Favorites, verbose_name='Теги фейворитов')
    registration_date = models.DateTimeField("Дата регистрации профиля", auto_now=True)

    def __str__(self) -> str:
        return f"Подробная информация профиля {self.profile.user.username}"

    class Meta:
        verbose_name = "Информация о профиле"
        verbose_name_plural = "Информации о профилях"

