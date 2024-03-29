from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


#Changes made from the diagram : 
#   Removed endate from Bid and changed Start to Time (for the exact time the bid was placed)
#   Haven't done it but maybe change price in Item to startPrice
#   Admin account is : admin, test


class User(AbstractUser):

    city = models.CharField(max_length=255,blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    picture = models.ImageField(upload_to="profileimages/", blank=True, null=True)

    
    def __str__(self) -> str:
        return("ID : " + str(self.id) + ", Username : " + self.username + ", Fname : " + self.first_name + ", Sname : " + self.last_name)  

    def to_dict(self) -> dict:
        """Returns a dictionary of item contents"""

        return {
            'id': self.id,
            'username': self.username,
            'fname' : self.first_name,
            'sname': self.last_name,
            'email' : self.email,
            'city' : self.city,
            'dob' : self.dob,
            'picture' : self.picture.url,
        } 
    

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)

    NEW = 'NEW'
    EXCELLENT = 'UE'
    GOOD= 'UG'
    OK='UA'
    Type = [
        (NEW, 'NEW'),
        (EXCELLENT, 'USED - EXCELLENT'),
        (GOOD, 'USED - GOOD'),
        (OK, 'USED - ACCEPTABLE'),
    ]
    condition = models.CharField(
        max_length=20,
        choices=Type,
        default=NEW,
    )


    # condition = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    start = models.DateField('Start Date')
    end = models.DateField('End Date')
    #picture = models.CharField(max_length=255)
    picture = models.ImageField(upload_to="itemimages/", blank=True, null=True)
    sold = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE , null=True)

    def __str__(self)->str:
        #return ("ID : " + str(self.id) + ", Name : " + self.name + ", Condition : " + self.condition + ", Price : " + str(self.price) + ", Start : " + str(self.start) + ", End : " + str(self.end) + ", Sold : " + str(self.sold) + ", Owner : " + str(self.owner))        
        return ("ID : " + str(self.id) + ", Name : " + self.name)

    def to_dict(self) ->dict:
        """Returns a dictionary of item contents"""

        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'condition': self.condition,
            'price': self.price,
            'start': self.start,
            'end':self.end,
            'picture':self.picture.url,
            'sold':self.sold,
            'owner':self.owner.to_dict()
        }

class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    time = models.DateTimeField('Bid time')
    amount = models.DecimalField(max_digits=10,decimal_places=2)


    def __str__(self)->str:
        #return ("ID : " + str(self.id) + ", Bidder : " + str(self.bidder) + ", Item : " + str(self.item) + ", Time : " + str(self.time) + ", Amount : " + str(self.amount))
        return ("ID : " + str(self.id) + ", Bidder : " + str(self.bidder) + ", Item : " + str(self.item))
    def to_dict(self)->dict:
        """Returns a dictionary of Bid contents"""
        return {
            'id': self.id,
            'bidder': self.bidder.to_dict(),
            'item': self.item.to_dict(),
            'time': self.time.strftime("%Y/%m/%d-%H:%M:%S"),
            'amount':self.amount,
        }


class Question(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    response = models.TextField(max_length=1000,default=None, blank=True, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    questioner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self)->str:
        #return ("ID : " + str(self.id) + ", Title : " + str(self.title) + ", Description : " + str(self.description) + ", Response : " + str(self.response) + ", Item : " + str(self.item) + ", Questioner : " + str(self.questioner))
        return ("ID : " + str(self.id) + ", Title : " + str(self.title))

    def to_dict(self)->dict:
        """Returns a dictionary of Question contents"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'response': self.response,
            'item': self.item.to_dict(),
            'questioner':self.questioner.to_dict(),
        }

