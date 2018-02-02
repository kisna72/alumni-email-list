from django.db import models

# Create your models here.
class University(models.Model):
	university = models.TextField()#Name of the university



class Alumni(models.Model):
	first_name = models.CharField(max_length = 200)
	last_name = models.CharField(max_length = 200)
	email_address =  models.EmailField()
	phone_number = models.TextField()
	graduation_year = models.IntegerFiend()
	graduation_month = models.ChoiceField()

class WorkHistory(models.Model):
	company_name = models.TextField()
	work_email = models.EmailField()
	position = models.TextField()
	alumni = models.ForeignKey(Alumni)


