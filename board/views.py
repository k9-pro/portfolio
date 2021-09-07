from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.response import Response
from django.db.models import Count,F,Q
from .models import Post,Notice,Notice_hit,Free,Post_comment,Post_reply,Free_comment,Free_reply,Free_hit,Post_hit,Post_good
from camp.models import Site
from drf_yasg import openapi
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from . import serializers
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import permission_classes
# Create your views here.

class PostData(viewsets.ModelViewSet) :
    """
        후기 CRUD
    """
    queryset = Post.objects.select_related("site","user")
    filter_backends = [SearchFilter, OrderingFilter,filters.DjangoFilterBackend]
    filterset_fields = ['site',] #사이트 종속 필터
    search_fields = ['title', 'content', 'user__username'] # full word search filter
    ordering_fields = ["created_at"] # 정렬

    my_tags = ["후기"] # swagger tag

    def get_serializer_class(self) :
        if self.action in ("list", "retrieve") : # 조회
            return serializers.ReadPostSerializer
        elif self.action in ("create") : # 쓰기
            return serializers.CreatePostSerializer
        elif self.action in ("partial_update") : # 수정
            if self.request.method == "PATCH" : # 필드 개별 수정
                return serializers.PatchPostSerializer
            return serializers.UpdatePostSerializer

        return serializers.ReadPostSerializer

class PostHitData(viewsets.ModelViewSet) :
    """
        후기 조회기록 CR
    """
    queryset = Post_hit.objects.values('ip','post_id').distinct()

    filter_backends = [OrderingFilter, filters.DjangoFilterBackend]
    filterset_fields = ['post', ]  # 후기 종속 필터
    ordering_fields = ["created_at"]  # 정렬

    my_tags = ["후기 조회기록"] # swagger tag

    def get_serializer_class(self) :
        if self.action in ("list", "retrieve") : # 조회
            return serializers.ReadPostHitSerializer
        elif self.action in ("create") : # 쓰기
            return serializers.CreatePostHitSerializer

        return serializers.ReadPostHitSerializer



class PostGoodData(viewsets.ModelViewSet) :
    """
        후기 추천 CR
    """
    queryset = Post_good.objects.values('user_id','post_id').distinct()

    filter_backends = [OrderingFilter, filters.DjangoFilterBackend]
    filterset_fields = ['post', ]  # 후기 종속 필터
    ordering_fields = ["created_at"]  # 정렬

    my_tags = ["후기 추천기록"] # swagger tag

    def get_serializer_class(self) :
        if self.action in ("list", "retrieve") : # 조회
            return serializers.ReadPostGoodSerializer
        elif self.action in ("create") : # 쓰기
            return serializers.CreatePostGoodSerializer

        return serializers.ReadPostGoodSerializer


class PostCommentData(viewsets.ModelViewSet) :
    """
        후기 댓글 CRUD
    """
    queryset = Post_comment.objects.select_related("post", "user")
    filter_backends = [OrderingFilter,filters.DjangoFilterBackend]
    filterset_fields = ['post', ]  # 후기 종속 필터
    ordering_fields = ["created_at"]  # 정렬

    my_tags = ["후기 댓글"]  # swagger tag

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):  # 조회
            return serializers.ReadPostCommentSerializer
        elif self.action in ("create"):  # 쓰기
            return serializers.CreatePostCommentSerializer
        elif self.action in ("partial_update"):  # 수정
            return serializers.UpdatePostCommentSerializer

        return serializers.ReadPostCommentSerializer

class PostReplyData(viewsets.ModelViewSet) :
    """
        후기 댓글 답변 CRUD
    """
    queryset = Post_reply.objects.select_related("post_comment", "user")
    filter_backends = [OrderingFilter, filters.DjangoFilterBackend]
    filterset_fields = ['post_comment', ]  # 후기 댓글 종속 필터
    ordering_fields = ["created_at"]  # 정렬

    my_tags = ["후기 댓글 답변"]  # swagger tag

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):  # 조회
            return serializers.ReadPostReplySerializer
        elif self.action in ("create"):  # 쓰기
            return serializers.CreatePostReplySerializer
        elif self.action in ("partial_update"):  # 수정
            return serializers.UpdatePostReplySerializer

        return serializers.ReadPostReplySerializer



class NoticeData(viewsets.ModelViewSet) :
    """
        공지사항 CRUD
    """
    queryset = Notice.objects.select_related("site","user")
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    filterset_fields = ['site', ]  # 사이트 종속 필터
    search_fields = ['title', 'content', 'user__username']  # full word search filter
    ordering_fields = ["created_at"]  # 정렬

    my_tags = ["공지사항"] # swagger tag

    def get_serializer_class(self) :
        if self.action in ("list", "retrieve") : # 조회
            return serializers.ReadNoticeSerializer
        elif self.action in ("create") : # 쓰기
            return serializers.CreateNoticeSerializer
        elif self.action in ("partial_update") : # 수정
            if self.request.method == "PATCH" : # 필드 개별 수정
                return serializers.PatchNoticeSerializer
            return serializers.UpdateNoticeSerializer

        return serializers.ReadNoticeSerializer

class NoticeHitData(viewsets.ModelViewSet) :
    """
        공지사항 조회기록 CR
    """
    queryset = Notice_hit.objects.values('ip','notice_id').distinct()

    filter_backends = [OrderingFilter, filters.DjangoFilterBackend]
    filterset_fields = ['notice', ]  # 공지사항 종속 필터
    ordering_fields = ["created_at"]  # 정렬

    my_tags = ["공지사항 조회기록"] # swagger tag

    def get_serializer_class(self) :
        if self.action in ("list", "retrieve") : # 조회
            return serializers.ReadNoticeHitSerializer
        elif self.action in ("create") : # 쓰기
            return serializers.CreateNoticeHitSerializer

        return serializers.ReadNoticeHitSerializer



class FreeData(viewsets.ModelViewSet) :
    """
        자유게시판 CRUD
    """
    # permission_classes = [permissions.DjangoModelPermissions]
    queryset = Free.objects.select_related("site","user")
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    filterset_fields = ['site', ]  # 사이트 종속 필터
    search_fields = ['title', 'content', 'user__username']  # full word search filter
    ordering_fields = ["created_at"]  # 정렬

    my_tags = ["자유게시판"] # swagger tag

    def get_serializer_class(self) :
        if self.action in ("list", "retrieve") : # 조회
            return serializers.ReadFreeSerializer
        elif self.action in ("create") : # 쓰기
            return serializers.CreateFreeSerializer
        elif self.action in ("partial_update") : # 수정
            if self.request.method == "PATCH" : # 필드 개별 수정
                return serializers.PatchFreeSerializer
            return serializers.UpdateFreeSerializer

        return serializers.ReadFreeSerializer


class FreeHitData(viewsets.ModelViewSet) :
    """
        자유게시판 조회기록 CR
    """
    queryset = Free_hit.objects.values('ip','free_id').distinct()

    filter_backends = [OrderingFilter, filters.DjangoFilterBackend]
    filterset_fields = ['free', ]  # 자유게시판 종속 필터
    ordering_fields = ["created_at"]  # 정렬

    my_tags = ["자유게시판 조회기록"] # swagger tag

    def get_serializer_class(self) :
        if self.action in ("list", "retrieve") : # 조회
            return serializers.ReadFreeHitSerializer
        elif self.action in ("create") : # 쓰기
            return serializers.CreateFreeHitSerializer

        return serializers.ReadFreeHitSerializer



class FreeCommentData(viewsets.ModelViewSet) :
    """
        자유게시판 댓글 CRUD
    """
    queryset = Free_comment.objects.select_related("free", "user")
    filter_backends = [OrderingFilter, filters.DjangoFilterBackend]
    filterset_fields = ["free"]  # 자유게시판 종속 필터

    ordering_fields = ["created_at"]  # 정렬

    my_tags = ["자유게시판 댓글"]  # swagger tag

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):  # 조회
            return serializers.ReadFreeCommentSerializer
        elif self.action in ("create"):  # 쓰기
            return serializers.CreateFreeCommentSerializer
        elif self.action in ("partial_update"):  # 수정
            return serializers.UpdateFreeCommentSerializer

        return serializers.ReadFreeCommentSerializer


class FreeReplyData(viewsets.ModelViewSet) :
    """
        자유게시판 댓글 답변 CRUD
    """
    queryset = Free_reply.objects.select_related("free_comment", "user")
    filter_backends = [OrderingFilter, filters.DjangoFilterBackend]
    filterset_fields = ['free_comment', ]  # 지유게시판 댓글 종속 필터
    ordering_fields = ["created_at"]  # 정렬

    my_tags = ["자유게시판 댓글 답변"]  # swagger tag

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):  # 조회
            return serializers.ReadFreeReplySerializer
        elif self.action in ("create"):  # 쓰기
            return serializers.CreateFreeReplySerializer
        elif self.action in ("partial_update"):  # 수정
            return serializers.UpdateFreeReplySerializer

        return serializers.ReadFreeReplySerializer



@swagger_auto_schema(
    method='get',
    tags=['추천 후기 베스트'],
)
@api_view(['GET'])
def BestPostData(request) :
    """
        추천 후기 베스트
    """
    queryset = Post.objects.filter(~Q(photo = '') & ~Q(photo__isnull=True)).annotate(
        good_count = Count('children_good__user_id', distinct=True),
        username = F('user__username'),
        sitename = F('site__name'),
        siteid = F('site__id')
    ).values('id', 'title', 'photo', 'username', 'siteid', 'sitename', 'good_count','created_at').distinct().order_by('-good_count','created_at')[:10]

    return Response(queryset)
