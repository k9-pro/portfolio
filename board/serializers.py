from rest_framework import serializers
from django.contrib.auth.models import User
from camp.models import Site, Location, Profile
from camp.serializers import ReadCampSerializer,UserSerializer
from django.db.models import F
from .models import Post,Notice,Notice_hit,Free,Post_comment,Free_comment,Post_reply,Free_reply,Free_hit,Post_hit,Post_good

"""
    베스트 후기
"""
class BastPostSerializer(serializers.ModelSerializer) :
    # class Meta :
        # model = Post_good

        # count =
        # fields = ('user_id')
    site = ReadCampSerializer(Site, fields=('id','name',))
    user = UserSerializer(User, fields=('username',))

    good_count = serializers.SerializerMethodField()

    class Meta :
        model = Post
        fields = ('id', 'site', 'user', 'good_count', 'photo', 'title', 'content', 'created_at')
        # ordering = ["created_at"]

    def get_good_count(self, obj):
        return obj.children_good.values('user_id','post_id').distinct().count()

"""
    후기 
"""
class ReadPostSerializer(serializers.ModelSerializer) :
    """
        후기 게시판 조회
        ___
    """
    site = ReadCampSerializer(Site, fields=('id','name',))
    user = UserSerializer(User, fields=('username','id'))

    hit = serializers.SerializerMethodField()
    good = serializers.SerializerMethodField()
    good_count = serializers.SerializerMethodField()

    class Meta :
        model = Post
        fields = ('id', 'site', 'user', 'hit', 'good', 'good_count', 'photo', 'title', 'content', 'created_at')
        # ordering = ["created_at"]

    def get_hit(self, obj):
        return obj.children_hit.values('ip','post_id').distinct().count()

    def get_good(self, obj):
        return obj.children_good.values('user_id','post_id').distinct()

    def get_good_count(self, obj):
        return obj.children_good.values('user_id','post_id').distinct().count()

class CreatePostSerializer(serializers.ModelSerializer) :
    """
        후기 등록
        ---
    """
    class Meta :
        model = Post
        fields = ('site','user','title','photo','content')

class UpdatePostSerializer(serializers.ModelSerializer) :
    """
        후기 수정
        ---
    """
    class Meta :
        model = Post
        fields = ('title','content','photo')

class PatchPostSerializer(serializers.ModelSerializer) :
    """
        후기 개별 필드 수정
        ---
    """
    class Meta :
        model = Post
        fields = ('title','content','photo')


"""
    후기 댓글
"""
class ReadPostCommentSerializer(serializers.ModelSerializer) :
    """
        후기 댓글 조회
        ___
    """
    user = UserSerializer(User, fields=('id','username',))
    reply = serializers.SerializerMethodField()

    class Meta :
        model = Post_comment
        fields = ('id','post','user', 'reply', 'content','created_at')

    def get_reply(self, obj):
        return obj.children_post_reply.annotate(username = F('user__username'), userid = F('user__id')).values('id', 'userid', 'username','content','created_at')

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
    후기 조회 기록
"""
class ReadPostHitSerializer(serializers.ModelSerializer) :
    """
        후기 조회기록 조회
        ___
    """

    class Meta :
        model = Post_hit
        fields = ('id','ip','created_at')

class CreatePostHitSerializer(serializers.ModelSerializer) :
    """
        후기 조회기록 등록
        ---
    """
    class Meta :
        model = Post_hit
        fields = ('post','ip')
        read_only_fields = ('ip',)

    def create(self, validated_data):
        x_forwarded_for = self.context.get('request').META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            validated_data['ip'] = x_forwarded_for.split(',')[0]
        else:
            validated_data['ip'] = self.context.get('request').META.get("REMOTE_ADDR")

        return Post_hit.objects.create(**validated_data)


"""
    후기 추천 기록
"""
class ReadPostGoodSerializer(serializers.ModelSerializer) :
    """
        후기 추천 기록 조회
        ___
    """

    class Meta :
        model = Post_good
        fields = ('id','user_id','post_id','created_at')

class CreatePostGoodSerializer(serializers.ModelSerializer) :
    """
        후기 추천 기록 등록
        ---
    """
    class Meta :
        model = Post_good
        fields = ('post','user')





"""
    공지 사항
"""
class ReadNoticeSerializer(serializers.ModelSerializer) :
    """
        공지사항 게시판 조회
        ___
    """
    site = ReadCampSerializer(Site, fields=('name',))
    user = UserSerializer(User, fields=('username','id'))
    # children = ReadNoticeHitSerializer(many=True, read_only=True)

    hit = serializers.SerializerMethodField()

    class Meta :
        model = Notice
        fields = ('id','site','user', 'hit','title','content','created_at')

    def get_hit(self, obj):
        return obj.children.values('ip','notice_id').distinct().count()


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
        fields = ('title','content')


"""
    공지 사항 조회 기록
"""
class ReadNoticeHitSerializer(serializers.ModelSerializer) :
    """
        공지사항 조회기록 조회
        ___
    """

    class Meta :
        model = Notice_hit
        fields = ('id','ip','created_at')


class CreateNoticeHitSerializer(serializers.ModelSerializer) :
    """
        공지사항 조회기록 등록
        ---
    """
    class Meta :
        model = Notice_hit
        fields = ('notice','ip')
        read_only_fields = ('ip',)

    def create(self, validated_data):
        x_forwarded_for = self.context.get('request').META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            validated_data['ip'] = x_forwarded_for.split(',')[0]
        else:
            validated_data['ip'] = self.context.get('request').META.get("REMOTE_ADDR")

        return Notice_hit.objects.create(**validated_data)



"""
    자유 게시판
"""
class ReadFreeSerializer(serializers.ModelSerializer) :
    """
        자유 게시판 조회
        ___
    """
    site = ReadCampSerializer(Site, fields=('name',))
    user = UserSerializer(User, fields=('username','id'))

    hit = serializers.SerializerMethodField()

    class Meta :
        model = Free
        fields = ('id', 'site', 'user', 'hit', 'title', 'content', 'created_at')

    def get_hit(self, obj):
        return obj.children.values('ip','free_id').distinct().count()

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
        fields = ('title','content')


"""
    자유게시판 댓글
"""
class ReadFreeCommentSerializer(serializers.ModelSerializer) :
    """
        자유게시판 댓글 조회
        ___
    """
    user = UserSerializer(User, fields=('id', 'username',))
    reply = serializers.SerializerMethodField()

    class Meta :
        model = Free_comment
        fields = ('id','free','user', 'reply', 'content', 'created_at')

    def get_reply(self, obj):
        return obj.children_free_reply.annotate(username = F('user__username'), userid = F('user__id')).values('id', 'userid', 'username','content','created_at')



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


"""
    자유게시판 사항 조회 기록
"""
class ReadFreeHitSerializer(serializers.ModelSerializer) :
    """
        자유게시판 조회기록 조회
        ___
    """

    class Meta :
        model = Free_hit
        fields = ('id','ip','created_at')

class CreateFreeHitSerializer(serializers.ModelSerializer) :
    """
        자유게시판 조회기록 등록
        ---
    """
    class Meta :
        model = Free_hit
        fields = ('free','ip')
        read_only_fields = ('ip',)

    def create(self, validated_data):
        x_forwarded_for = self.context.get('request').META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            validated_data['ip'] = x_forwarded_for.split(',')[0]
        else:
            validated_data['ip'] = self.context.get('request').META.get("REMOTE_ADDR")

        return Free_hit.objects.create(**validated_data)