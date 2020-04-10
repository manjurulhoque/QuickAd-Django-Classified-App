from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class AdImage(models.Model):
    image = models.ImageField(verbose_name="Ad image", upload_to="ad_images")


class Ad(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Ad title")
    price = models.IntegerField(verbose_name="Ad price")
    description = models.TextField(verbose_name="Ad description")
    ad_image = models.ForeignKey(AdImage, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
