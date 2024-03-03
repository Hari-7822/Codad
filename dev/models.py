from django.db import models
from datetime import datetime
from django.utils import timezone


class OTPVerification(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    otp_key = models.CharField(max_length=6)  # Adjust the max_length as needed
    updated_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"OTPVerification(id={self.id}, otp_key={self.otp_key}, updated_time={self.updated_time})"
    

class Applicant(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=8)
    preferred_internship_domain = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    whatsapp_number = models.CharField(max_length=15)
    highest_academic_qualification = models.CharField(max_length=255)
    current_year = models.IntegerField()
    where_learned_about_codad = models.CharField(max_length=255)
    joined_using = models.CharField(max_length=15)
    accept_terms = models.BooleanField()
    Intern_completed = models.BooleanField(default=False)       # to check the person completed the Intern
    Paid = models.BooleanField(default=False)                   # to check the person paid for internship or not
    updated_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
