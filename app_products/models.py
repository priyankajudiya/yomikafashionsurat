from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_delete
from django.dispatch import receiver
# Create your models here.


############################## Category List
class category(models.Model):
    productCategory = models.CharField(max_length=50)

    def __str__(self):
        return self.productCategory

############################## Products Model
def img_path(instance, filename):
    path = f'products/{instance.seller}/product_{instance.id}/{filename}'
    return path


class product(models.Model):
    cat = models.ForeignKey(category, on_delete = models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=150, blank=True, null=True)

    img1 = models.ImageField(upload_to=img_path, blank=True)
    img2 = models.ImageField(upload_to=img_path, blank=True)
    img3 = models.ImageField(upload_to=img_path, blank=True)

    title = models.CharField(max_length=60)
    price = models.IntegerField()
    size = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    desc = models.CharField(max_length=555)
    fabric = models.CharField(max_length=20, blank=True)
    work = models.CharField(max_length=50, blank=True)
    style = models.CharField(max_length=200, blank=True)
    occasion = models.CharField(max_length=200, blank=True)

    def save(self, *args, **kwargs ):
        self.slug = slugify(self.title)
        try:
            this = product.objects.get(id=self.id)
            if this.img1 != self.img1:
                this.img1.delete()
            if this.img2 != self.img2:
                this.img2.delete()
            if this.img3 != self.img3:
                this.img3.delete()
        except:
            pass

        super(product, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk)

###################################################### Function to delete image on delete Post
@receiver(post_delete, sender=product)
def delete_image_with_post(sender, instance, **kwargs):
    instance.img1.delete(False)
    instance.img2.delete(False)
    instance.img3.delete(False)
