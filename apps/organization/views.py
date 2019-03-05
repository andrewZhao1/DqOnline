from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from .models import CityDict, CourseOrg
from .forms import UserAskForm
from courses.models import Course
from operation.models import UserFavorite


class OrgView(View):
    '''
    课程机构列表功能
    '''

    def get(self, request):
        # 课程机构
        all_orgs = CourseOrg.objects.all()
        hot_orgs = all_orgs.order_by('-click_nums')[:5]

        # 城市
        all_citys = CityDict.objects.all()

        # 取出篩選城市
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id = int(city_id))

        # 類別篩選
        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category = category)

        org_nums = all_orgs.count()

        # 排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by('-students')
            elif sort == 'courses':
                all_orgs = all_orgs.order_by('-course_nums')

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, 4, request=request)
        orgs = p.page(page)

        return render(request, 'org-list.html', {
            'all_orgs': orgs,
            'all_citys': all_citys,
            'org_nums': org_nums,
            'city_id': city_id,
            'category': category,
            'hot_orgs': hot_orgs,
            'sort': sort
        })

class AddUserAskView(View):
    '''
    用户添加咨询
    '''
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit = True)
            return HttpResponse('{"status" : "success"}', content_type = 'application/json')
        else:
            return HttpResponse('{"status" : "fail", "msg" : "添加错误"}', content_type = 'application/json')

class OrgHomeView(View):
    '''
    机构首页
    '''
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        #判断用户是否登录，显示实际收藏结果
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        all_courses = course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:3]
        return render(request, 'org-detail-homepage.html', {
            'all_courses' : all_courses,
            'all_teachers' : all_teachers,
            'course_org' : course_org,
            'has_fav' : has_fav,
            'current_page' : 'home',
            })

class OrgCourseView(View):
    '''
    机构课程
    '''
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        #判断用户是否登录，显示实际收藏结果
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        all_courses = course_org.course_set.all()
        return render(request, 'org-detail-course.html', {
            'all_courses' : all_courses,
            'course_org' : course_org,
            'has_fav' : has_fav,
            'current_page' : 'course',
            })

class OrgDescView(View):
    '''
    机构介绍
    '''
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        #判断用户是否登录，显示实际收藏结果
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        all_courses = course_org.course_set.all()
        return render(request, 'org-detail-desc.html', {
            'all_courses' : all_courses,
            'course_org' : course_org,
            'has_fav' : has_fav,
            'current_page' : 'desc',
            })

class OrgTeacherView(View):
    '''
    机构讲师
    '''
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        #判断用户是否登录，显示实际收藏结果
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        all_teachers = course_org.teacher_set.all()
        return render(request, 'org-detail-teachers.html', {
            'all_teachers' : all_teachers,
            'course_org' : course_org,
            'has_fav' : has_fav,
            'current_page' : 'teacher',
            })

class AddFavView(View):
    '''
    收藏/取消收藏
    '''
    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)

        if not request.user.is_authenticated:
            return HttpResponse('{"status" : "fail", "msg" : "用户未登录"}', content_type = 'application/json')

        exist_record = UserFavorite.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
        if exist_record:
            #已经存在，则取消收藏
            exist_record.delete()
            return HttpResponse('{"status" : "success", "msg" : "收藏"}', content_type = 'application/json')
        else:
            user_fav = UserFavorite()
            if int(fav_id) > 0 and int(fav_type) > 0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()
                return HttpResponse('{"status" : "success", "msg" : "已收藏"}', content_type = 'application/json')
            else:
                return HttpResponse('{"status" : "fail", "msg" : "收藏出错"}', content_type = 'application/json')


        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit = True)
            return HttpResponse('{"status" : "success"}', content_type = 'application/json')
        else:
            return HttpResponse('{"status" : "fail", "msg" : "添加错误"}', content_type = 'application/json')