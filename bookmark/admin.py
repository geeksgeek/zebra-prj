# bookmark/admin.py

from django.contrib import admin
from .models import Bookmark

class BookmarkAdmin(admin.ModelAdmin):
	list_display = ['title', 'url']

admin.site.register(Bookmark, BookmarkAdmin)

'''
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
	list_display = ['title', 'url']
'''

