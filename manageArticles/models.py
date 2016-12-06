from django.db import models
from django.core.urlresolvers import reverse


class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Entry(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body = models.TextField()
    bodyfull = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    category = models.CharField(max_length=100)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    image1 = models.ImageField(upload_to="images/beerthumbs/", help_text="50x180px image") 
    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title + self.author + self.category 

    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]
