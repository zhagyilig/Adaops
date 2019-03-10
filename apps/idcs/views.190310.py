import logging
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import IDC
from .serializers import IdcSerializers

logger = logging.getLogger(__name__)


class JsonResponse(HttpResponse):
    """
    自己封装JsonResponse
    """

    def __init__(self, data, **kwargs):
        kwargs.setdefault('content_type', 'application/json')
        # 解析成 json 数据
        data = JSONRenderer().render(data)
        super(JsonResponse, self).__init__(content=data, **kwargs)


##################################  版本一  ##################################

def idc_list(request, *args, **kwargs):
    """ 列出所有 idc 记录 """
    if request.method == 'GET':
        queryset = IDC.objects.all()
        # 序列化
        serializer = IdcSerializers(queryset, many=True)
        # 解析成json
        # 1.
        # content = JSONRenderer().render(serializer.data)
        # return HttpResponse(content, content_type='application/json')
        # 2.
        return JsonResponse(serializer.data, status=200)

    elif request.method == 'POST':
        data = JSONParser().parse(request)  # 只接收 json 数据
        print(data)
        serializer = IdcSerializers(data=data)  # 序列化
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.data)


def idc_detail(request, pk, *args, **kwargs):
    """ idc 详细信息及操作 """
    try:
        idc = IDC.objects.get(pk=pk)
    except IDC.DoesNotExist:
        return HttpResponse(status=400)

    if request.method == 'GET':
        # 序列化
        serializer = IdcSerializers(idc)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        # 接收 json 数据
        content = JSONParser().parse(request)
        serializer = IdcSerializers(idc, data=content)
        # 数据有效性判断
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.data, status=400)

    elif request.method == 'DELETE':
        idc.delete()
        return HttpResponse(status=200)


##################################  版本二  ##################################
from rest_framework.decorators import api_view  # 包装API
from rest_framework import status  # 状态码
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET', 'POST'])
def idc_list_v2(request, *args, **kwargs):
    """ 列出所有 idc 记录 """
    if request.method == 'GET':
        # 获取数据
        queryset = IDC.objects.all()
        # 序列化
        serializer = IdcSerializers(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # POST 的数据
        print(request.data)
        # 序列化
        serializer = IdcSerializers(data=request.data)
        # 验证数据有效性
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def idc_detail_v2(request, pk, *args, **kwargs):
    """ idc 详细信息及操作 """
    try:
        idc = IDC.objects.get(pk=pk)
    except IDC.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  # Response

    if request.method == 'GET':
        # 序列化
        serializer = IdcSerializers(idc)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # 接收 json 数据
        serializer = IdcSerializers(idc, data=request.data)  # 提交的数据全部在 request.data
        # 数据有效性判断
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        idc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def api_root(reqest, format=None, *args, **kwargs):
    return Response({
        'idcs': reverse('idc_list', request=reqest, format=format),
    })


##################################  版本三  ##################################
from rest_framework.views import APIView
from django.http import Http404


class VIdcList(APIView):
    def get(self, request, format=None):
        queryset = IDC.objects.all()
        serizlizer = IdcSerializers(queryset, many=True)
        return Response(serizlizer.data)

    def post(self, request, format=None):
        serializer = IdcSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Respons(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class VIdcDetail(APIView):
    def get_object(self, pk):
        try:
            return IDC.objects.all(pk=pk)
        except IDC.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        idc = IDC.objects.get(pk=pk)
        serialzer = IdcSerializers(idc)
        return Response(serialzer.data)

    def put(self, request, pk, format=None):
        idc = self.get_object(pk)
        serializer = IdcSerializers(idc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        idc = self.get_object(pk)
        idc.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


##################################  版本四  ##################################
from rest_framework import mixins, generics


class IdcList_v4(generics.GenericAPIView,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin):
    queryset = IDC.objects.all()
    serializer_class = IdcSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class IdcDetail_v4(generics.GenericAPIView,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    queryset = IDC.objects.all()
    serializer_class = IdcSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, *kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, *kwargs)



##################################  版本五  ##################################
from rest_framework import viewsets

class IdcListViewset(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.CreateModelMixin):

    queryset = IDC.objects.all()
    serializer_class = IdcSerializers


##################################  版本六  ##################################
from rest_framework import viewsets
class IdcViewset_v6(viewsets.ModelViewSet):
    queryset = IDC.objects.all()
    serializer_class = IdcSerializers

