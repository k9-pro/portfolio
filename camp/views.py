from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Site
from .serializers import ReadCampSerializer, WriteCampSerializer

# Create your views here.
# @api_view(['GET'])
# def testAPI(request):
#     return Response("test!!!")



class CampData(viewsets.ModelViewSet):
    """
        캠핑장 정보
    """
    """
        select_related : 사용하려는 객체가 정참조(다른 객체의 ForeignKey를 가지고 있음) 혹은
                        ForeignKey가 없더라도 1:1 관계에 있는 객체의 데이터를 캐싱해 오는 메소드이다.
        select_related를 쓰면 해당 객체 외 해당객체가 참조하는 데이터들이 한 꺼번에 불러와줘 매번 DB에 접속해서 해당 데이터를 불러오지 않아도 된다.
        Debugger도구로 확인해 보면 다른 객체에 연결되어 있는 ForeignKey(id값)으로 조인으로 연결되어 있음을 할 수 있다.
    """
    queryset = Site.objects.select_related("user","location")
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name','address','user__username','location__name']
    ordering_fields = ["created_at"]
    my_tags = ["캠핑장 정보"]

    def get_serializer_class(self) :
        if self.action in ("list", "retrieve") :
            return ReadCampSerializer
        return WriteCampSerializer
        # serializer_class = ReadCampSerializer

