from email.policy import default
from importlib.resources import contents
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length = 30)

    def __str__(self):
        return self.caption 


class Standings(models.Model):
    standings_slug = models.SlugField(unique=True, db_index=True, null=True)
    position = models.IntegerField(null=True, default=1)
    logo = models.ImageField(upload_to = "media", null=True)
    club = models.CharField(max_length=200)
    MP = models.IntegerField()
    GD = models.IntegerField()
    pts = models.IntegerField()
    stadium = models.CharField(max_length=200, default="Ethiad")
    stadium_img = models.ImageField(upload_to = "media", null=True)
    founded = models.IntegerField(null=True)
    manager = models.CharField(max_length=200, null=True)
    website = models.URLField(null=True)
    text = models.TextField(null=True)
    fact_one = models.CharField(max_length=500, null=True)
    fact_two = models.CharField(max_length=500, null=True)
    fact_three = models.CharField(max_length=500, null=True)


class Post(models.Model):
    title = models.CharField(max_length = 100)
    excerpt = models.CharField(max_length = 1000)
    image = models.ImageField(upload_to = "media", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(100)])
    tags = models.ManyToManyField(Tag)

class Comment(models.Model):
    user_name=models.CharField(max_length=120)
    user_email=models.EmailField()
    text=models.TextField(max_length=300)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
