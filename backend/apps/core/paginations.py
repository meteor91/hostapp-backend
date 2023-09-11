from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.response import Response


class LimitOffsetPaginationExtended(LimitOffsetPagination):
    ordering = 'created_at'

    def get_paginated_response(self, data):
        return Response({
            'total': self.count,
            'limit': self.limit,
            'offset': self.offset,
            'results': data
        })


class StandardPageNumberPagination(PageNumberPagination):
    ordering = 'created_at'
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = 'page_number'

    def get_paginated_response(self, data):
        return Response({
            'page_number': self.page.number,
            'page_size': self.page_size,
            'total_elements': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })
