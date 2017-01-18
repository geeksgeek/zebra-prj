# blog/views.py

from django.views.generic import ListView, DetailView
from django.views.generic.dates import (
	ArchiveIndexView, YearArchiveView, MonthArchiveView,
	DayArchiveView, TodayArchiveView
)

from .models import Post

class PostLV(ListView):
	model = Post
	paginate_by = 2

class PostDV(DetailView):
	model = Post
	date_field = 'modify_date'

class PostYAV(YearArchiveView):
	model = Post
	date_field = 'modify_date'
	make_object_list = True

class PostMAV(MonthArchiveView):
	model = Post
	date_field = 'modify_date'

class PostDAV(DayArchiveView):
	model = Post
	date_field = 'modify_date'

class PostTAV(TodayArchiveView):
	model = Post
	date_field = 'modify_date'


