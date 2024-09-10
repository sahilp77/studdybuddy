from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=200)

    
    def __str__(self):
        return self.name

class Room(models.Model):
    #host 
    host = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete= models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, max_length=10000)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-create_at','-updated_at']
    
    
    def __str__(self):
        return self.name
    
    
class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}: {self.body[:20]}"