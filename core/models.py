from django.db import models

class WorkExperience(models.Model):
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    _from = models.DateField()
    _to = models.DateField()
    current = models.BooleanField(default=True)


class Education(models.Model):  
    university_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    _from = models.DateField()
    _to = models.DateField()


class Certificate(models.Model):
    name = models.CharField(max_length=255)
    certificate_number = models.CharField(max_length=255)
    issued_date = models.DateField()
    expiration_date = models.CharField(max_length=100)
    attachment = models.FileField(upload_to='files')


# class Language(models.Model):
#     pass


# class Skill(models.Model):
#     pass


# class Voluntarism(models.Model):
#     pass



