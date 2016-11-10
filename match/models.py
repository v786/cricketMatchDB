from django.db import models

# Create your models here.

class Team(models.Model):
	name = models.CharField(max_length = 20)
	country = models.CharField(max_length = 20)
	score = models.IntegerField(default=0)
	def __str__(self):
		return self.name
	def lead(self):
		return score

class Player(models.Model):
	Team = models.ForeignKey(Team, on_delete = models.CASCADE)
	name = models.CharField(max_length=40)
	dob = models.DateTimeField('date published')
	runs = models.IntegerField(default = 0)
	balls_faced = models.IntegerField(default = 0)
	jersey = models.IntegerField(default = 0)
	def __str__(self):
		return self.name
	def born(self):
		return self.dob

class Tournament(models.Model):
	name = models.CharField(max_length=40)
	start_date = models.DateTimeField('date published')
	end_date = models.DateTimeField('date published')
	num_team = models.IntegerField(default = 0)
	def __str__(self):
		return self.name
	def no_team(self):
		return self.num_team




