from django.contrib import admin
from .models import Language, Profile, Gallery, Photo, ProfileInformation, Favorites
from django.contrib.admin.widgets import AdminFileWidget
from django.db import models
from django.utils.safestring import mark_safe

admin.site.register(Profile)

class AdminPhotoWidget(AdminFileWidget):
    def render(self, name, value, attrs = None, renderer=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" width="150" height="150"  style="object-fit: cover;"/></a>' % (image_url, image_url, file_name))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


class PhotoInline(admin.TabularInline):
    model = Photo
    formfield_overrides = {models.ImageField: {'widget': AdminPhotoWidget}}
    extra = 3

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("profile",)
    list_display_links = ("profile",)
    inlines = (PhotoInline,)

admin.site.register(Photo)
admin.site.register(Favorites)
admin.site.register(ProfileInformation)
admin.site.register(Language)
