from django.contrib import admin

from .models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
	list_display = ('username', 'activity_type', 'duration_minutes', 'workout_date', 'calories_burned')
	search_fields = ('username', 'activity_type')
