from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    #these are the attributes that we want to override for PageNumberPagination
    page_size_query_param = 'page_size'
    page_query_param = 'page-num'
    max_page_size = 2

    #override the funtion
    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'results': data,
        })