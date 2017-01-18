# bookmark/views.py

from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render
from .models import Bookmark

# Class Based View
class BookmarkLV(ListView):
	model = Bookmark

bookmark_list = BookmarkLV.as_view()

'''
# Function Based View
def bookmark_list(request):
	context = {'bookmark_list': Bookmark.objects.all()}
	return render(request, 'bookmark/bookmark_list.html', context)
'''

# Class Based View
class BookmarkDV(DetailView):
	model = Bookmark

bookmark_detail = BookmarkDV.as_view()

''' 
# Function Based View
def bookmark_detail(request, pk):
	context = {'bookmark': bookmark}
	return render(request, 'bookmark/bookmark_detail.html', context)   
'''
