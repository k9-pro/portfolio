from django.db import models
from django.contrib.auth.models import User
from camp.models import Site
# Create your models here.

class Notice(models.Model) :
    """
        공지 사항
    """
    site = models.ForeignKey(Site, on_delete=models.CASCADE, help_text='캠핑장정보 FK')
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='작성자 FK')
    title = models.CharField(max_length=150, help_text='제목', db_index=True)
    content = models.TextField(null=True, blank=True, help_text='내용')
    hit = models.IntegerField(default=0, help_text='조회수')
    created_at = models.DateTimeField(auto_now_add=True, help_text='생성일시')
    updated_at = models.DateTimeField(auto_now=True, help_text='수정일시')
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self) :
        return self.title

class Post(models.Model) :
    """
        후기
    """
    site = models.ForeignKey(Site, on_delete=models.CASCADE, help_text='캠핑장정보 FK')
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='작성자 FK')
    title = models.CharField(max_length=150, help_text='제목', db_index=True)
    content = models.TextField(null=True, blank=True, help_text='내용')
    hit = models.IntegerField(default=0, help_text='조회수')
    good = models.IntegerField(default=0, help_text='추천수', db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, help_text='생성일시')
    updated_at = models.DateTimeField(auto_now=True, help_text='수정일시')
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self) :
        return self.title

class Post_comment(models.Model) :
    """
        후기 댓글
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, help_text='후기 FK')
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='작성자 FK')
    content = models.TextField(help_text='내용')
    created_at = models.DateTimeField(auto_now_add=True, help_text='생성일시')
    updated_at = models.DateTimeField(auto_now=True, help_text='수정일시')
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self) :
        return self.content

class Post_reply(models.Model) :
    """
        후기 댓글 답변
    """
    post_comment = models.ForeignKey(Post_comment, on_delete=models.CASCADE, help_text='후기 댓글 FK')
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='작성자 FK')
    content = models.TextField(help_text='내용')
    created_at = models.DateTimeField(auto_now_add=True, help_text='생성일시')
    updated_at = models.DateTimeField(auto_now=True, help_text='수정일시')
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self) :
        return self.content



class Free(models.Model) :
    """
        자유 게시판
    """
    site = models.ForeignKey(Site, on_delete=models.CASCADE, help_text='캠핑장정보 FK')
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='작성자 FK')
    title = models.CharField(max_length=150, help_text='제목', db_index=True)
    content = models.TextField(null=True, blank=True, help_text='내용')
    hit = models.IntegerField(default=0, help_text='조회수')
    created_at = models.DateTimeField(auto_now_add=True, help_text='생성일시')
    updated_at = models.DateTimeField(auto_now=True, help_text='수정일시')
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self) :
        return self.title


class Free_comment(models.Model):
    """
        자유게시판 댓글
    """
    free = models.ForeignKey(Free, on_delete=models.CASCADE, help_text='자유게시판 FK')
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='작성자 FK')
    content = models.TextField(help_text='내용')
    created_at = models.DateTimeField(auto_now_add=True, help_text='생성일시')
    updated_at = models.DateTimeField(auto_now=True, help_text='수정일시')
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.content


class Free_reply(models.Model):
    """
        자유게시판 댓글 답변
    """
    free_comment = models.ForeignKey(Free_comment, on_delete=models.CASCADE, help_text='자유게시판 댓글 FK')
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='작성자 FK')
    content = models.TextField(help_text='내용')
    created_at = models.DateTimeField(auto_now_add=True, help_text='생성일시')
    updated_at = models.DateTimeField(auto_now=True, help_text='수정일시')
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.content