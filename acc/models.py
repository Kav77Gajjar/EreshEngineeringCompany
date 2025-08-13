from django.db import models
from django.utils.text import slugify

class HeroSection(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    hero_image_url = models.URLField(blank=True, null=True)
    website = models.URLField("Optional Field", blank=True, null=True)
    brand_name = models.CharField(max_length=20, blank=True, null=True)
    brand_logo = models.URLField()
    hero_name = models.CharField(max_length=10, blank=True, null=True)
    hero_name_description = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Main Page Landing Section"

    def __str__(self):
        return self.title

class AboutMe(models.Model):
    title = models.CharField(max_length=100)
    img_url_for_about = models.URLField(blank=True, null=True)
    content = models.TextField()

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    image_url = models.URLField(blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    service_image_url = models.URLField()

    class Meta:
        verbose_name = "Our Service"
        verbose_name_plural = "Our Services"

    def __str__(self):
        return self.title



class SocialLinks(models.Model):
    title = models.CharField('AddSocialLinksBelow', max_length=50, blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Social Media Links"
        verbose_name_plural = "Social Media Links"

    def __str__(self):
        return self.title