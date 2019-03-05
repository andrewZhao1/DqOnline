from django.urls import path, include
from .views import CoursesView

app_name='course'
urlpatterns = [
    # 课程列表页
    path('list/', CoursesView.as_view(), name='course_list'),
    path('detail/<int:course_id>', CoursesView.as_view(), name='course_detail'),
    
]