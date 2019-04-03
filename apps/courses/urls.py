from django.urls import path, include
from .views import CoursesView, CourseDetailView, CourseInfoView, CourseCommentView, CourseCommentAddView

app_name = 'course'
urlpatterns = [
    # 课程列表页
    path('list/', CoursesView.as_view(), name='course_list'),
    path('detail/<int:course_id>', CourseDetailView.as_view(), name='course_detail'),
    path('info/<int:course_id>', CourseInfoView.as_view(), name='course_info'),
    path('comments/<int:course_id>', CourseCommentView.as_view(), name='course_comments'),
    path('add_comment/', CourseCommentAddView.as_view(), name='add_comment'),

]
