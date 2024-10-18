from django.db import models

# Create your models here.
GENDER_CHOICES = [
    ('M','Male'),
    ('F','Female'),
    ('O','Other')
 ]

PARTY_CHOISES = [
    ('BJP','Bharatiya Janata Party'),
    ('Congress','Congress'),
    ('Shiv Sena','Shiv Sena'),
    ('Shiv Sena Thackeray','Shiv Sena Uddhav Balasaheb Thackeray'),
    ('Rashtrawadi Congress','Rashtrawadi Congress'),
    ('Manase','Maharashtra Navnirman Sena')
]

class Newregistration(models.Model):
    fullname = models.CharField(max_length=200)
    dob = models.DateField()
    sex = models.CharField(choices=GENDER_CHOICES, max_length=30)
    city = models.CharField(max_length=30)
    taluka = models.CharField(max_length=30)
    dist = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.IntegerField()
    addharno = models.IntegerField()
    voterid = models.IntegerField()
    mobno = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.fullname

class Voterregistration(models.Model):
    fullname = models.CharField(max_length=200)
    dob = models.DateField()
    sex = models.CharField(choices=GENDER_CHOICES, max_length=10)
    city = models.CharField(max_length=30)
    taluka = models.CharField(max_length=30)
    dist = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.IntegerField()
    addharno = models.IntegerField()
    voterid = models.IntegerField()
    mobno = models.IntegerField()
    email = models.EmailField()
    partynm = models.CharField(choices=PARTY_CHOISES,max_length=50, null=True, blank=True)
    partyimg = models.ImageField(upload_to='images/',null=True, blank=True)
# null=True, blank=True
    def __str__(self):
        return self.fullname

class Completedvote(models.Model):
    voterid = models.IntegerField()
    fullname = models.CharField(max_length=200)
    vote = models.CharField(default='none', max_length=100)

    def __str__(self):
        return self.fullname

class Result(models.Model):
    fullname = models.CharField(max_length=200)
    partynm = models.CharField(max_length=50)
    partyimg = models.ImageField(upload_to='images/',)
    vote = models.IntegerField(default=0)