from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Site, Location, Profile

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
        직렬 변환기가 초기화되면 직렬 변환기에 설정된 필드 사전은 .fields속성을 사용하여 액세스할 수 있습니다 . 이 속성에 액세스하고 수정하면 직렬 변환기를 동적으로 수정할 수 있습니다.
        fields인수를 직접 수정하면 직렬 변환기를 선언하는 시점이 아니라 런타임에 직렬 변환기 필드의 인수를 변경하는 것과 같은 흥미로운 작업을 수행할 수 있습니다.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class ProfileSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Profile
        fields = ('alias', 'gender')

class UserSerializer(DynamicFieldsModelSerializer) :
    profile = ProfileSerializer()
    class Meta :
        model = User
        fields = ('username', 'profile')

        # def __init__(self,)
class LocationSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Location
        fields = ('name',)

class WriteCampSerializer(serializers.ModelSerializer) :

    # location = serializers.SlugRelatedField(slug_field='location_id', queryset=Location.objects.all())
    class Meta :
        model = Site
        fields = ('name', 'note', 'address', 'is_state', 'created_at', 'updated_at')

class ReadCampSerializer(DynamicFieldsModelSerializer) :
    user = UserSerializer()
    location = LocationSerializer()
    class Meta :
        model = Site
        fields = ('name', 'note', 'address', 'is_state', 'created_at', 'updated_at','user','location')
        read_only_fields = fields
    # def validate_email(self) :
    #     data = self.get_initial()
    #     raise serializers.ValidationError("test")
    #     return value
    # def create(self, ):