from django.db import models

# Create your models here.

class Personal_Details(models.Model):
    Name = models.CharField(max_length=100)
    Father_Name = models.CharField(max_length=100)
    Mother_Name = models.CharField(max_length=100)
    Contact_Number = models.CharField(max_length=10)
    Emergency_Number = models.CharField(max_length=10)
    Present_Address = models.CharField(max_length=100)
    Permanent_Address = models.CharField(max_length=100)
    Qualification = models.CharField(max_length=100)
    
class Employee_Profiles(models.Model):
    employee_data = models.ForeignKey(Personal_Details, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone = models.CharField(max_length=10)
    Dob = models.DateField()
    Blood_Group = models.CharField(max_length=25)
    
    def add_name(self):
        self.name = self.First_Name + ' ' + self.Last_Name
        return self.name
    

    # employees = models.ManyToManyField(Employee, related_name='departments')

class Employment_History(models.Model):
    Previous_CompanyName = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Date_of_Employment = models.CharField(max_length=100)
    Experience = models.CharField(max_length=100)
    Present_Address = models.CharField(max_length=100)
    Achievements = models.CharField(max_length=100)
    Qualification = models.CharField(max_length=100)

class Salary_Management(models.Model):
    pass 

