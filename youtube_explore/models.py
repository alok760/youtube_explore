from django.db import models

# Create your models here.
class Video(models.Model):
    # artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    # name = models.CharField(max_length=100)
    # release_date = models.DateField()
    # num_stars = models.IntegerField()
    # TODO: add indexes
    video_id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    etag = models.CharField(max_length=100) #signifies change
    channel_id = models.CharField(max_length=100)
    channel_title = models.CharField(max_length=100, db_index=True)
    published_at = models.DateTimeField(max_length=100, null=True, db_index=True)
    thumbnail_url = models.CharField(max_length=100, null=True)