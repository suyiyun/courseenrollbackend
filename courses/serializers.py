from dataclasses import field
from rest_framework import serializers
from courses.models import Course

'''
class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    course_name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    course_location = serializers.CharField(required=True, allow_blank=False, max_length=30)
    course_content = serializers.CharField(required=True, allow_blank=False, max_length=200)
    teacher_id = serializers.IntegerField(required=True, allow_blank=False)

    def create(self, validate_data):
        return Course.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.course_name = validate_data.get('course_name', instance.course_name)
        instance.course_location = validate_data.get('course_location', instance.course_location)
        #...
        return instance
'''
#  更简单的方法 ModelSerializer
class CourseSerializer(serializers.ModelSerializer):
    class Meta: #inner class from rest framework documentation
        model = Course
        fields = ['id', 'course_name', 'course_location', 'course_content', 'teacher_id']
        # fields = '__all__'
