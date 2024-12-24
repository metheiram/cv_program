from django.db import models

class User(models.Model):
    userID = models.CharField(max_length=50, primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class Skill(models.Model):
    skillID = models.CharField(max_length=50, primary_key=True)
    skillName = models.CharField(max_length=100)

    def __str__(self):
        return self.skillName

class UserSkill(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    skillID = models.ForeignKey(Skill, on_delete=models.CASCADE)

class Reference(models.Model):
    referenceID = models.CharField(max_length=50, primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name

class WorkExperience(models.Model):
    experienceID = models.CharField(max_length=50, primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    companyName = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    startYear = models.IntegerField()
    endYear = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.companyName} - {self.role}"

class Contact(models.Model):
    contactID = models.CharField(max_length=50, primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.phone

class Education(models.Model):
    educationID = models.CharField(max_length=50, primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    startYear = models.IntegerField()
    endYear = models.IntegerField()

    def __str__(self):
        return f"{self.degree} from {self.institution}"

