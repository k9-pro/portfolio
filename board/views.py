from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.response import Response
from .models import Post,Notice,Free,Post_comment,Post_reply,Free_comment,Free_reply
from camp.models import Site
from drf_yasg import openapi
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from . import serializers
# from .serializers import ReadPostSerializer,CreatePostSerializer,UpdatePostSerializer,PatchPostSerializer
# from .serializers import ReadPostCommentSerializer,CreatePostCommentSerializer,UpdatePostCommentSerializer
# from .serializers import ReadNoticeSerializer,CreateNoticeSerializer,UpdateNoticeSerializer,PatchNoticeSerializer
# from .serializers import ReadFreeSerializer,CreateFreeSerializer,UpdateFreeSerializer,PatchFreeSerializer
# Create your views here.

class PostData(viewsets.ModelViewSet) :
    """
        후기 CRUD
    """
    queryset = Post.objects.select_related("site","user")
    filter_backends = [SearchFilter, OrderingFilter,filters.DjangoFilterBackend]
    filterset_fields = ['site',] #사이트 종속 필터
    search_fields = ['title', 'content', 'user__username'] # full word search filter
    ordering_fields = ["-created_at"] # 정렬

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


class PostCommentData(viewsets.ModelViewSet) :
    """
        후기 댓글 CRUD
    """
    queryset = Post_comment.objects.select_related("post", "user")
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['post', ]  # 후기 종속 필터
    ordering_fields = ["-created_at"]  # 정렬

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
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['post_comment', ]  # 후기 댓글 종속 필터
    ordering_fields = ["-created_at"]  # 정렬

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
    ordering_fields = ["-created_at"]  # 정렬

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



class FreeData(viewsets.ModelViewSet) :
    """
        자유게시판 CRUD
    """
    queryset = Free.objects.select_related("site","user")
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    filterset_fields = ['site', ]  # 사이트 종속 필터
    search_fields = ['title', 'content', 'user__username']  # full word search filter
    ordering_fields = ["-created_at"]  # 정렬

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

class FreeCommentData(viewsets.ModelViewSet) :
    """
        자유게시판 댓글 CRUD
    """
    queryset = Free_comment.objects.select_related("free", "user")
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ["free"]  # 자유게시판 종속 필터

    ordering_fields = ["-created_at"]  # 정렬

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
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['free_comment', ]  # 지유게시판 댓글 종속 필터
    ordering_fields = ["-created_at"]  # 정렬

    my_tags = ["자유게시판 댓글 답변"]  # swagger tag

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):  # 조회
            return serializers.ReadFreeReplySerializer
        elif self.action in ("create"):  # 쓰기
            return serializers.CreateFreeReplySerializer
        elif self.action in ("partial_update"):  # 수정
            return serializers.UpdateFreeReplySerializer

        return serializers.ReadFreeReplySerializer