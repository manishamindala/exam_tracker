import os

class Config:
    SECRET_KEY = 'your-very-secret-key-here'
    # This creates a file named exam_tracker.db in your project folder
    SQLALCHEMY_DATABASE_URI = 'sqlite:///exam_tracker.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False