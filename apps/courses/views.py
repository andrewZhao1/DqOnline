from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from .models import Course


class CoursesView(View):
	def get(self, request):
		all_courses = Course.objects.all()
		try:
			page = request.GET.get('page', 1)
		except PageNotAnInteger:
			page = 1
		p = Paginator(all_courses, 9, request=request)
		courses = p.page(page)
		return render(request, 'course-list.html', {
			'all_courses': courses
			})

