from django.db import models
from datetime import datetime    

# Create your models here.
class getData(models.Model):
  SAMPLECHOICES = (
    ("yes","yes"),
    ("no","no")
    )
  # request_id=models.AutoField(primary_key=True)
  firstname=models.CharField(max_length=50,default="first_name")
  lastname=models.CharField(max_length=50,default="last_name")
  email=models.EmailField( max_length=254,default="error@gmail.com")
  test=models.IntegerField(default=0)
  image=models.ImageField(upload_to="foodimages/",default="foodimages/1072416.jpg")
  testchoices=models.CharField(max_length=3,choices=SAMPLECHOICES)
  date_created=models.DateTimeField(blank=True,default=datetime.now())
  

  def __str__(self):
    return self.firstname+self.lastname

