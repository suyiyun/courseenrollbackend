from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from courses.models import Course
from courses.serializers import CourseSerializer
from rest_framework.exceptions import APIException

# Create your views here.
class UserCourseViewSet(viewsets.ViewSet):
    
    # def get_user(self):
    #     user_name = 'admin'
    #     password = 'admin'
    #     return authenticate(username=user_name, password=password)
    
    permission_class = (IsAuthenticated, ) # tuple, permission_classes 是一个viewset下的属性

    # 列出当前用户所有已选课程
    # 1. http method (CRUD) ? read -> GET
    # 2. url?   /user/courses http://127.0.0.1:8000/user/courses
    # 3. user input? (student id) no input as we use jwt
    # 4. response data/code ? courses list, 200
    @action(methods=["GET"], detail=False)
    def courses(self, request):
        # TODO: read courses list from database
        # user = self.get_user()
        user = request.user #rest_framework work
        enrolled_courses = user.courses.all()   #object -> "[{key1: value, key2: value}]"
        #serialize object
        serializer = CourseSerializer(enrolled_courses, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    # 学生添加一门课程
    # 1. http method (CRUD) ? Create -> POST 考虑数据库 是一对一还是一对多 还是多对多
    # 2. url?   /user/course/<course_name> http://127.0.0.1:8000/user/course/OOD/
    # 3. user input:  course name(passed in the url) (student id 可以直接通过jwt token拿到)
    # 4. response data/code ? enrolled course name, 200/ no response 204
    @action(methods=["POST"], detail=False, url_path="course/(?P<course_name>[\w\s]+)")
    def course(self, request, **kwargs): #**kwargs 类似于js...]
        course_name = kwargs['course_name']
        # TODO: connect db to enroll a course
        # get user object
        # user = self.get_user()
        user = request.user
        course = Course.objects.filter(course_name=course_name).first()
        # sanity check
        if course is None:
            raise APIException('course does not exist')

        if user in course.user.all():
            raise APIException('course has already been enrolled')
        #enroll a course
        course.user.add(user)
        return Response({}, status.HTTP_204_NO_CONTENT)

    # 学生删除一门课程
    # 1. http method (CRUD) ? delete -> DELETE 考虑数据库 是一对一还是一对多 还是多对多
    # 2. url?   /user/course/<course_name> http://127.0.0.1:8000/user/course/OOD/
    # 3. user input:  course name(passed in the url) (student id 可以直接通过jwt token拿到)
    # 4. response data/code ? enrolled course name, 200/ no response 204
    @course.mapping.delete
    def drop_course(self, request, **kwargs):
        course_name = kwargs['course_name']
        # user = self.get_user()
        user = request.user
        course = Course.objects.filter(course_name=course_name).first()
        if course is None:
            raise APIException('course does not exist')

        if user not in course.user.all():
            raise APIException('Course has not been enrolled by current user')
        #delete a course
        course.user.remove(user)
        return Response({}, status.HTTP_204_NO_CONTENT)

class CourseViewSet(viewsets.ViewSet):
    # 列出所有课程
    # 1. http method (CRUD) ? read -> GET 考虑数据库 是一对一还是一对多 还是多对多
    # 2. url?   /courses http://127.0.0.1:8000/courses
    # 3. user input:  
    # 4. response data/code: course
    @action(methods=["GET"], detail=False)
    def courses(self, request):
        # TODO: read all courses from database
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

class UserInfoViewSet(viewsets.ViewSet):
    # 修改学生的手机号 （一个学生只有一个手机号）
    # 1. http method (CRUD) ? update -> PUT put是用于专属一对一 因为是一对一
    # 2. url?   /user/phone_number PUT http://127.0.0.1:8000/user/phone_number/
    # 3. user input:  phone number (sensitive data) put into request body 只要传参传在body里都是用post
    # 4. response data/code: no response 204 
    @action(methods=["PUT"], detail=False)
    def phone_number(self, request):
        # when you send form-encoded body data, always use request.POST
        phone_number = request.POST.get('phone_number') 
        # TODO: connect db to udate a course
        return Response("Updated phone number %s" % phone_number, status.HTTP_204_NO_CONTENT)
