from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=20, unique=True, db_index=True)

    def __str__(self):
        return(self.title)


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
