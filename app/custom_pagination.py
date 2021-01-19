from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size_query_param = 'pageSize'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'meta': {
                'total_count': self.page.paginator.count,
                'page_size': self.get_page_size(self.request),
                'page_count': self.page.paginator.num_pages,
                'page_number': self.page.number,
                'previous_page': self.get_previous_page_number(),
                'next_page': self.get_next_page_number(),
            },
            'results': data
        })

    def get_previous_page_number(self):
        if self.page.number == 1:
            return None
        return self.page.previous_page_number()

    def get_next_page_number(self):
        if self.page.paginator.num_pages == self.page.number:
            return None
        return self.page.next_page_number()
