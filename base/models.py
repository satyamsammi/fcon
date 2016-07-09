from django.db import models
REVIEW_CHOICES = (('5', 'Very Good'), ('4', 'Good'),('3', 'Average'),('2', 'Poor'), ('1','Very Poor'))
# Create your models here.

def productphotoname(instance,filename):
	ext = filename.split('.')[-1]
	name = filename.split('.')[0]
	return str('products/'+instance.title+'/images/'+name+'.'+ext)


class HomeImages(models.Model):
	image = models.ImageField(upload_to="home/")
	def __str__(self):
		return str(self.image)

class Product(models.Model):	
	title = models.CharField(unique = True, max_length=30)
	overview = models.CharField(max_length=1000)
	
	hotcount = models.IntegerField(default = 0)
	image = models.ImageField(upload_to=productphotoname,blank=False,null=False)
	def __str__(self):
		return "%s" %(self.title)



class Review(models.Model):
	title = models.CharField(max_length = 30)
	description = models.CharField(max_length = 5000)
	creator_name = models.CharField(max_length = 70)
	creator_contact_no = models.IntegerField(default = 91,blank=True, null=True)
	creator_email = models.EmailField()
	creator_rating = models.CharField(max_length = 30, choices=REVIEW_CHOICES, default = REVIEW_CHOICES[0][0])
	created_on = models.DateTimeField(auto_now_add=True)
	is_visible = models.BooleanField(default=False)
	def __str__(self):
		return str(self.title)

def reviewphotoname(instance,filename):
	ext = filename.split('.')[-1]
	name = filename.split('.')[0]
	x = instance.review.title.strip()
	return 'review/'+x+'/images/'+name+'.'+ext

class ReviewImages(models.Model):
	review = models.ForeignKey(Review)
	image = models.ImageField(upload_to = reviewphotoname)
	def __str__(self):
		return "%s %s" %(self.review.title, self.id)
