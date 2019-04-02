# coding=utf-8
# auth: zhangyiling
# time: 2019-03-21 22:05
# description: 覆盖rest_framework.permissions.DjangoModelPermissions

from rest_framework.permissions import DjangoModelPermissions


class Permissions(DjangoModelPermissions):
    # 直接copy源代码
    perms_map = {
        'GET': ['%(app_label)s.change_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_permission(self, request, view):
        # Workaround to ensure DjangoModelPermissions are not applied
        # to the root view when using DefaultRouter.
        if getattr(view, '_ignore_model_permissions', False):
            return True

        if not request.user or (
           not request.user.is_authenticated and self.authenticated_users_only):
            return False

        queryset = self._queryset(view)
        perms = self.get_required_permissions(request.method, queryset.model)

        print('++++++++++{}'.format(perms))
        return request.user.has_perms(perms)

