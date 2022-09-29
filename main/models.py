from django.db import models
from django.contrib.auth.models import User


class MessMenu(models.Model):
    day = models.CharField(max_length=20,null=True,blank=True)
    breakfast = models.TextField(null=True,blank=True)
    breakfast_price = models.CharField(max_length=4,null=True,blank=True)
    lunch = models.TextField(null=True,blank=True)
    lunch_price = models.CharField(max_length=4,null=True,blank=True)
    dinner = models.TextField(null=True,blank=True)
    dinner_price = models.CharField(max_length=4,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Mess Menu'
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.day} Menu'


class StudentLeave(models.Model):
    user = models.OneToOneField(User, related_name="student_leave_user", on_delete=models.CASCADE)
    place_visiting = models.CharField(max_length=20,null=True,blank=True)
    departure_date = models.CharField(max_length=20, null=True,blank=True)
    arrival_date = models.CharField(max_length=20,null=True,blank=True)
    reason = models.TextField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Student Leave'
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.user} Leave Details'

class Hostel(models.Model):
    hostel_name = models.CharField(max_length=20,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Hostels'
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.hostel_name} Hostel'

class College(models.Model):
    college_name = models.CharField(max_length=100,null=True,blank=True)
    students = models.ManyToManyField(User, blank=True)
    fee_amount = models.DecimalField(max_digits = 8, decimal_places=2, blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Colleges'
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.college_name}'

class FeePaid(models.Model):
    amount = models.DecimalField(max_digits = 8, decimal_places=2, blank=True,null=True)
    student_id = models.CharField(max_length=20,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True, blank=True)
    class Meta:
        verbose_name_plural = 'FeesPaid'
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.student_id} paid {self.amount}'

class FeeRecords(models.Model):
    student_id = models.CharField(max_length=20,null=True,blank=True)
    student_name = models.CharField(max_length=50,null=True,blank=True)
    college = models.CharField(max_length=100,null=True,blank=True)
    amount_paid = models.DecimalField(max_digits = 8, decimal_places=2, blank=True,null=True)
    balance = models.CharField(max_length=10,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True, blank=True)
    class Meta:
        verbose_name_plural = 'FeesRecords'
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.student_name} fee balance {self.balance}'