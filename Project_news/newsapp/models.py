from django.db import models

# Create your models here.
class Top_headline(models.Model):
	source_name = models.CharField(max_length=512)
	auther = models.CharField(max_length=512)
	title = models.TextField(unique=True, null=False)
	description = models.TextField()
	url = models.TextField()
	urlToImage = models.TextField()
	publishedAt = models.CharField(max_length=256)
	content = models.TextField()
	category = models.CharField(max_length=256)
	initial_score = models.FloatField()
	upload_date = models.CharField(max_length=256)

	def __str__(self):
		return self.title

class NewsSource(models.Model):
	name = models.CharField(unique=True, max_length=512)
	description= models.TextField()
	url = models.TextField()

	def __str__(self):
		return self.name

