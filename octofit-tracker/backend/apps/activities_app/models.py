from django.db import models


class Activity(models.Model):
	username = models.CharField(max_length=150)
	activity_type = models.CharField(max_length=100)
	duration_minutes = models.PositiveIntegerField()
	workout_date = models.DateField()
	calories_burned = models.PositiveIntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-workout_date', '-created_at']

	def __str__(self):
		return f'{self.username} - {self.activity_type}'
