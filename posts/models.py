from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


# photo or video
class PostMedia(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.FileField(
        upload_to="uploads/",
        validators=[FileExtensionValidator(allowed_extensions=["mp4", "jpeg"])]
    )
