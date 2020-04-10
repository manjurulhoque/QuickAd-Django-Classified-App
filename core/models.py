from django.db import models

from accounts.models import User


class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    title = models.CharField(max_length=255)
    image = models.ImageField(verbose_name="Category Image", upload_to="category_images",
                              default="category_images/default.png")

    def __str__(self):
        return self.title


class AdImage(models.Model):
    image = models.ImageField(verbose_name="Ad image", upload_to="ad_images")


class Ad(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Ad title")
    price = models.IntegerField(verbose_name="Ad price")
    description = models.TextField(verbose_name="Ad description")
    ad_image = models.ForeignKey(AdImage, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
