from rest_framework import serializers
from django.contrib.auth.models import User
from camp.models import Site, Location, Profile
from camp.serializers import ReadCampSerializer,UserSerializer
from .models import Post,Notice,Free,Post_comment,Free_comment,Post_reply,Free_reply


"""
    후기 
"""
class ReadPostSerializer(serializers.ModelSerializer) :
    """
        후기 게시판 조회
        ___
    """
    site = ReadCampSerializer(Site, fields=('id','name',))
    user = UserSerializer(User, fields=('username',))

    class Meta :
        model = Post
        fields = ('id','site','user','title','content','hit','good','created_at')

class CreatePostSerializer(serializers.ModelSerializer) :
    """
        후기 등록
        ---
    """
    class Meta :
        model = Post
        fields = ('site','user','title','content')

class UpdatePostSerializer(serializers.ModelSerializer) :
    """
        후기 수정
        ---
    """
    class Meta :
        model = Post
        fields = ('title','content')

class PatchPostSerializer(serializers.ModelSerializer) :
    """
        후기 개별 필드 수정
        ---
    """
    class Meta :
        model = Post
        fields = ('title','content','hit','good')


"""
    후기 댓글
"""
class ReadPostCommentSerializer(serializers.ModelSerializer) :
    """
        후기 댓글 조회
        ___
    """
    user = UserSerializer(User, fields=('username',))

    class Meta :
        model = Post_comment
        fields = ('id','post','user','content','created_at')

class CreatePostCommentSerializer(serializers.ModelSerializer) :
    """
        후기 댓글 등록
        ---
    """
    class Meta :
        model = Post_comment
        fields = ('post','user','content')

class UpdatePostCommentSerializer(serializers.ModelSerializer) :
    """
        후기 댓글 수정
        ---
    """
    class Meta :
        model = Post_comment
        fields = ('content',)


"""
    후기 댓글 답변
"""
class ReadPostReplySerializer(serializers.ModelSerializer) :
    """
        후기 댓글 답변 조회
        ___
    """
    user = UserSerializer(User, fields=('username',))

    class Meta :
        model = Post_reply
        fields = ('id','post_comment','user','content','created_at')

class CreatePostReplySerializer(serializers.ModelSerializer) :
    """
        후기 댓글 답변 등록
        ---
    """
    class Meta :
        model = Post_reply
        fields = ('post_comment','user','content')

class UpdatePostReplySerializer(serializers.ModelSerializer) :
    """
        후기 댓글 답변 수정
        ---
    """
    class Meta :
        model = Post_reply
        fields = ('content',)


"""
    공지 사항
"""
class ReadNoticeSerializer(serializers.ModelSerializer) :
    """
        공지사항 게시판 조회
        ___
    """
    site = ReadCampSerializer(Site, fields=('name',))
    user = UserSerializer(User, fields=('username',))

    class Meta :
        model = Notice
        fields = ('id','site','user','title','content','hit','created_at')

class CreateNoticeSerializer(serializers.ModelSerializer) :
    """
        공지 등록
        ---
    """
    class Meta :
        model = Notice
        fields = ('site','user','title','content')

class UpdateNoticeSerializer(serializers.ModelSerializer) :
    """
        공지 수정
        ---
    """
    class Meta :
        model = Notice
        fields = ('title','content')

class PatchNoticeSerializer(serializers.ModelSerializer) :
    """
        공지 개별 필드 수정
        ---
    """
    class Meta :
        model = Notice
        fields = ('title','content','hit')



"""
    자유 게시판
"""
class ReadFreeSerializer(serializers.ModelSerializer) :
    """
        자유 게시판 조회
        ___
    """
    site = ReadCampSerializer(Site, fields=('name',))
    user = UserSerializer(User, fields=('username',))

    class Meta :
        model = Free
        fields = ('id','site','user','title','content','hit','created_at')

class CreateFreeSerializer(serializers.ModelSerializer) :
    """
        자유 게시판 등록
        ---
    """
    class Meta :
        model = Free
        fields = ('site','user','title','content')

class UpdateFreeSerializer(serializers.ModelSerializer) :
    """
        자유 게시판 수정
        ---
    """
    class Meta :
        model = Free
        fields = ('title','content')

class PatchFreeSerializer(serializers.ModelSerializer) :
    """
        자유 게시판 개별 필드 수정
        ---
    """
    class Meta :
        model = Free
        fields = ('title','content','hit')


"""
    자유게시판 댓글
"""
class ReadFreeCommentSerializer(serializers.ModelSerializer) :
    """
        자유게시판 댓글 조회
        ___
    """
    user = UserSerializer(User, fields=('username',))

    class Meta :
        model = Free_comment
        fields = ('id','free','user','content','created_at')

class CreateFreeCommentSerializer(serializers.ModelSerializer) :
    """
        자유게시판 댓글 등록
        ---
    """
    class Meta :
        model = Free_comment
        fields = ('free','user','content')

class UpdateFreeCommentSerializer(serializers.ModelSerializer) :
    """
        자유게시판 댓글 수정
        ---
    """
    class Meta :
        model = Free_comment
        fields = ('content',)


"""
    자유게시판 댓글 답변
"""
class ReadFreeReplySerializer(serializers.ModelSerializer) :
    """
        자유게시판 댓글 답변 조회
        ___
    """
    user = UserSerializer(User, fields=('username',))

    class Meta :
        model = Free_reply
        fields = ('id','free_comment','user','content','created_at')

class CreateFreeReplySerializer(serializers.ModelSerializer) :
    """
        자유게시판 댓글 답변 등록
        ---
    """
    class Meta :
        model = Free_reply
        fields = ('free_comment','user','content')

class UpdateFreeReplySerializer(serializers.ModelSerializer) :
    """
        자유게시판 댓글 답변 수정
        ---
    """
    class Meta :
        model = Free_reply
        fields = ('content',)