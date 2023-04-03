from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from pages.formatChecker import validate_file_size
# Create your models here.


class Sermon(models.Model):
    title = models.CharField(max_length=120)
    image_mobile = models.ImageField(upload_to='sermons/mobile/image', default='sermons/default.jpg')
    image_desktop = models.ImageField(upload_to='sermons/desktop/image', default='sermons/default.jpg')
    description = models.TextField()
    audio = models.FileField(upload_to='sermons/', blank=True, null=True, validators=[validate_file_size])
    date = models.DateField()
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def get_image_filename(self, filename):
        title = self.title
        slug = slugify(title)
        return "%s-%s" % (slug, filename)

    def save(self, *args, **kwargs):
        if self.image_mobile and self.image_desktop:
            self.image_mobile.name = self.get_image_filename(self.image_mobile.name)
            self.image_desktop.name = self.get_image_filename(self.image_desktop.name)
            self.image_url = self.image_mobile.url
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('sermons', kwargs={'id': self.id})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Sermons'
        unique_together = ('title', 'date')
class Announcement(models.Model):
    event_type = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    date = models.DateField()
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Galleries'
