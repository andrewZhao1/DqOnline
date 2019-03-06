from django.urls import path, include
from .views import CoursesView, CourseDetailView

app_name = 'course'
urlpatterns = [
    # 课程列表页
    path('list/', CoursesView.as_view(), name='course_list'),
    path('detail/<int:course_id>', CourseDetailView.as_view(), name='course_detail'),
    path('info/<int:course_id>', CourseDetailView.as_view(), name='course_info'),

]
