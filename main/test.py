from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Twitter
# Create your tests here.
User = get_user_model()

class TweetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='t1', password='123')
        self.userb = User.objects.create_user(username='t2', password='345')
        Twitter.objects.create(content="test1", 
            user=self.user)
        Twitter.objects.create(content="test2", 
            user=self.user)
        Twitter.objects.create(content="test2", 
            user=self.userb)
        self.currentCount = Twitter.objects.all().count()
        
    def test_tweet_created(self):
        tweet_obj = Twitter.objects.create(content="test3", 
            user=self.user)
        self.assertEqual(tweet_obj.id, 4)
        self.assertEqual(tweet_obj.user, self.user)
        
    def test_tweet_list(self):
        client = self.get_client()
        response = client.get("/api/main/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)
    
    def test_action_like(self):
        client = self.get_client()
        response = client.post("/api/main/action/", 
            {"id": 1, "action": "like"})
        count_like = response.json().get("likes")
        user = self.user
        like_instances_count = user.tweetlike_set.count()
        related_likes = user.tweet_user.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(like_instances_count, 1)
        self.assertEqual(like_instances_count, related_likes)
        self.assertEqual(count_like, 1)
