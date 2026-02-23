from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.activities_app.models import Activity  # Adjust if you have custom models for teams, leaderboard, workouts
from djongo import models as djongo_models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB directly for index creation
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        # Ensure unique index on email for users
        db.users.create_index([('email', 1)], unique=True)

        # Clear collections
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Sample users
        users = [
            {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
            {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
            {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
            {"name": "Black Widow", "email": "widow@marvel.com", "team": "Marvel"},
        ]
        db.users.insert_many(users)

        # Sample teams
        teams = [
            {"name": "Marvel", "members": ["ironman@marvel.com", "cap@marvel.com", "widow@marvel.com"]},
            {"name": "DC", "members": ["superman@dc.com", "batman@dc.com", "wonderwoman@dc.com"]},
        ]
        db.teams.insert_many(teams)

        # Sample activities
        activities = [
            {"user_email": "superman@dc.com", "activity": "Flying", "duration": 60},
            {"user_email": "batman@dc.com", "activity": "Martial Arts", "duration": 45},
            {"user_email": "ironman@marvel.com", "activity": "Flight Suit Training", "duration": 50},
            {"user_email": "cap@marvel.com", "activity": "Shield Throwing", "duration": 30},
        ]
        db.activities.insert_many(activities)

        # Sample leaderboard
        leaderboard = [
            {"team": "Marvel", "points": 150},
            {"team": "DC", "points": 140},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Sample workouts
        workouts = [
            {"name": "Strength Training", "suggested_for": ["Batman", "Captain America"]},
            {"name": "Agility Drills", "suggested_for": ["Black Widow", "Wonder Woman"]},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
