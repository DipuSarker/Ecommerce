from django.db import models

# Create your models here.

class Settings(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    fax = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    smtpserver = models.CharField(max_length=100)
    smtpemail = models.CharField(max_length=50, blank=True, null=True)
    smtppassword = models.CharField(max_length=100, blank=True)
    smtpport = models.CharField(max_length=100, blank=True)
    icon = models.ImageField(blank=True, null=True, upload_to='icon/')
    facebook = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    address = models.TextField()
    contact = models.TextField()
    reference = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    