from drf_yasg.inspectors import SwaggerAutoSchema
from rest_framework import viewsets
from rest_framework import serializers
from django.contrib.auth.models import User

class CustomAutoSchema(SwaggerAutoSchema):
    """
        Swagger auto schema 설정
        Swagger 태그로 api 분리하기 위해 필요
    """
    def get_tags(self, operation_keys=None):
        tags = self.overrides.get('tags', None) or getattr(self.view, 'my_tags', [])
        if not tags:
            tags = [operation_keys[0]]

        return tags


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"


