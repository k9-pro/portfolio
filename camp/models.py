from django.db import models
from django.contrib.auth.models import User,AbstractUser

# from .managers import CustomUserManager


class Location(models.Model) :
    """
        지역관련 테이블
    """
    name = models.CharField(max_length=80, help_text='지역명', db_index=True)

    def __str__(self) :
        return self.name


class Profile(models.Model) :
    """
        프로필 정보
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text='사용자 FK')
    alias = models.CharField(max_length=150, help_text='별칭', db_index=True)
    gender = models.CharField(
        max_length=2,
        choices=[('남', '남'), ('여','여')],
        help_text='성별'
    )

    def __str__(self) :
        return self.alias


class Site(models.Model) :
    """
        무료 캠핑장 정보 테이블
    """
    location = models.ForeignKey(Location, on_delete=models.CASCADE, help_text='지역 FK')
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='작성자 FK')
    name = models.CharField(max_length=150, help_text='캠핑장명', db_index=True)
    address = models.CharField(max_length=150, help_text='상세주소')
    is_state = models.CharField(
        max_length=5,
        choices=[('OPEN', 'OPEN'), ('CLOSE', 'CLOSE')],
        help_text='캠핑장 상태'
    )
    note = models.TextField(help_text='비고', null=True)
    created_at = models.DateTimeField(auto_now_add=True, help_text='생성일시')
    updated_at = models.DateTimeField(auto_now=True, help_text='수정일시')
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self) :
        return self.name
