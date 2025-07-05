from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="photos",
    )
    image = models.ImageField(
        upload_to="photos/",   # stored in MEDIA_ROOT/photos/
    )
    description = models.TextField(
        blank=True,            # caption is optional
    )

    def __str__(self) -> str:
        # avoid huge strings in the admin
        return self.description[:50] or f"Photo {self.pk}"
