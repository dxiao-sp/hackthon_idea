from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    year_published = models.CharField(max_length=10)
    review = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title 

class User(models.Model):
    name = models.CharField(max_length = 180)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Idea(models.Model):
    title = models.CharField(max_length = 180)
    description = models.CharField(max_length = 180)
    eventName = models.CharField(max_length = 180)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length = 180)
    description = models.CharField(max_length = 180)
    eventName = models.CharField(max_length = 180)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return self.comment