import os

def firebase_config(request):
    return {
        'firebase_config': os.getenv('FIREBASE_CONFIG'),
        'vapid_key': os.getenv('VAPID_KEY'),
    }