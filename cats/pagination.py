from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CatsPagination(PageNumberPagination):
    page_size = 3

    def get_paginated_response(self, data):
        return Response({'count': self.page.paginator.count, 'response': data})
