from django.contrib.auth.models import Group
from groups.serilaizers import GroupSerializer
from rest_framework import viewsets
from .groupsFilter import GroupFilter


class GroupsViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_class = GroupFilter
    filter_fields = ("name",)


