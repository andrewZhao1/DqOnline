from django.urls import path, include
from .views import UserInfoView, UploadImageView, ModifyPwdView, SendMailCodeView, UpdateEmailView, MyCourseView, \
    MyFavOrgView, MyFavCourseView, MyMessageView, MyFavTeacherView

app_name = 'organization'
urlpatterns = [
    # 个人中心
    path('info/', UserInfoView.as_view(), name='user_info'),
    path('mycourse/', MyCourseView.as_view(), name='mycourse'),
    path('myfav/org/', MyFavOrgView.as_view(), name='myfav_org'),
    path('myfav/teacher/', MyFavTeacherView.as_view(), name='myfav_teacher'),
    path('myfav/course/', MyFavCourseView.as_view(), name='myfav_course'),
    path('mymessage/', MyMessageView.as_view(), name='mymessage'),
    path('image/upload/', UploadImageView.as_view(), name='image_upload'),
    path('modify/pwd/', ModifyPwdView.as_view(), name='modify_pwd'),
    path('sendemail_code/', SendMailCodeView.as_view(), name='sendemail_code'),
    path('update_email/', UpdateEmailView.as_view(), name='update_email'),

]
