from django.db import models

# Create your models here.
class Fcuser(models.Model):
    email = models.EmailField(verbose_name="e-mail")
    password= models.CharField(max_length=64,verbose_name="Password")
    register_date= models.DateTimeField(auto_now_add=True,verbose_name="Register Time")

    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name='사용자'
        verbose_name_plural = '사용자'