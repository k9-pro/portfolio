from django.urls import path, include
from rest_framework import routers
from .views import PostData,NoticeData,FreeData,PostCommentData,FreeCommentData,PostReplyData,FreeReplyData,NoticeHitData,FreeHitData,PostHitData,PostGoodData,BestPostData

router = routers.DefaultRouter()

router.register(r'^post',PostData)
router.register(r'^post-hit',PostHitData)
router.register(r'^post-good',PostGoodData)
router.register(r'^postcomment',PostCommentData)
router.register(r'^postreply',PostReplyData)
router.register(r'^notice',NoticeData)
router.register(r'^notice-hit',NoticeHitData)
router.register(r'^free',FreeData)
router.register(r'^free-hit',FreeHitData)
router.register(r'^freecomment',FreeCommentData)
router.register(r'^freereply',FreeReplyData)



# router.register(r'^post/hit',PostHitData)
# router.register(r'',PostData)

urlpatterns = [
    path("",include(router.urls)),
    path("bestpost/", BestPostData),
    # path("free/",FreeData.as_view()),
    # path("post/",PostData),
]