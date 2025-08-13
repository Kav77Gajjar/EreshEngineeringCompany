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
    title = models.CharField(max_length=100, blank=True, null=True)
    img_url_for_about = models.URLField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

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

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    service_image_url = models.URLField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title

class ServiceFeature(models.Model):
    service = models.ForeignKey(Services,related_name="features" , on_delete=models.CASCADE)
    feature_text = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Service Feature"
        verbose_name_plural = "Service Features"

    def __str__(self):
        return f"{self.service.title} - {self.feature_text}"


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

class ContactInfo(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    email_title = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_title = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    whatsapp_title = models.CharField(max_length=50, blank=True, null=True)
    whatsapp = models.CharField(blank=True, null=True)

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"

    def __str__(self):
        return self.title
