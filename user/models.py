from django.db import models
from django.contrib.auth.models import User


class ProfessionalName(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class PersonalInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    twitter = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


class Skill(models.Model):
    description = models.TextField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.image.name


class UserInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    professional_names = models.ManyToManyField(ProfessionalName)
    services = models.ManyToManyField(Service)
    personal_information = models.OneToOneField(PersonalInformation, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)
    gallery_images = models.ManyToManyField(GalleryImage)
    total_clients = models.IntegerField()
    total_projects = models.IntegerField()
    total_awards = models.IntegerField()
    total_years_experience = models.IntegerField()
    address = models.TextField()
    facebook = models.CharField(max_length=255)
    name = models.CharField(max_length=255, default="admin")

    def __str__(self):
        return self.name
