from django.conf import settings
from django import forms
from .models import Tweet

max_twitter_len = settings.MAX_TWEET_LENGTH

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']
    
    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > max_twitter_len:
            raise forms.ValidationError("Exceed Length Limit")
        return content
