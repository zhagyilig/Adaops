# coding=utf-8
# auth: zhangyiling
# time: 2019-05-19 22:51
# description: 自定义分页

import logging
from rest_framework.pagination import PageNumberPagination

logger = logging.getLogger(__name__)


class Pagination(PageNumberPagination):
    """自定义分页类."""

    def get_page_size(self, request):
        """获取当前页码显示条目."""
        try:
            page_size = int(request.query_params.get('page_size', -1))
            if page_size < 0:
                return self.page_size
            return page_size
        except Exception as e:
            logging.error('自定义分页类:{}'.format(e.args))
        return self.page_size
