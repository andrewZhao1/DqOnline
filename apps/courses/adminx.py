import xadmin

from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
	list_display = ['name', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'add_time']
	search_fileds = ['name', 'detail', 'degree', 'students', 'fav_nums']
	list_filter = ['name', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'add_time']

class LessonAdmin(object):
	list_display = ['course', 'name', 'add_time']
	search_fileds = ['course', 'name']
	list_filter = ['course', 'name', 'add_time']

class VideoAdmin(object):
	list_display = ['lesson', 'name', 'add_time']
	search_fileds = ['lesson', 'name']
	list_filter = ['lesson', 'name', 'add_time']

class CourseResourceAdmin(object):
	list_display = ['course', 'name', 'download', 'add_time']
	search_fileds = ['course', 'name', 'download']
	list_filter = ['course', 'name', 'download', 'add_time']

xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)

