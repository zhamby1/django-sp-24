from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.

#create a Post model with an author, title, text, created date, published date

class Post(models.Model):
    #grab the author id from the users database.  If the user is deleted, it will delete all the posts associated with that user
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='10000')

    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title