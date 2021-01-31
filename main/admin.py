from django.contrib import admin
from .models import Twitter, TwitterModel


class TweetLikeAdmin(admin.TabularInline):
    model = TwitterModel

class TweetAdmin(admin.ModelAdmin):
    inlines = [TwitterModelAdmin]
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username', 'user__email']
    class Meta:
        model = Twitter

admin.site.register(Twitter, TwitterAdmin)
