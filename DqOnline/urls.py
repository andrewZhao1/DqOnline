"""DqOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.views.static import serve
import xadmin

from users.views import LoginView, RegisterView, UserActiveView, ForgetPwdView, ResetView, ResetPwdView
from organization.views import OrgView
from DqOnline.settings import MEDIA_ROOT

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='logout'),
    path('captcha/', include('captcha.urls')),
    path('active/<str:active_code>', UserActiveView.as_view(), name='user_active'),
    path('forget/', ForgetPwdView.as_view(), name='forget_pwd'),
    path('reset/<str:active_code>', ResetView.as_view(), name='user_reset'),
    path('reset_pwd/', ResetPwdView.as_view(), name='reset_pwd'),

    # 课程机构
    path('org/', include('organization.urls', namespace='org')),

    # 课程机构
    path('course/', include('courses.urls', namespace='course')),

    # 配置上传文件的访问地址
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),

]
