from rest_framework.pagination import PageNumberPagination, Response

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "limit"

    def get_paginated_response(self, data):
        return Response(
            {
                "count": self.page.paginator.count,
                "page": int(self.request.query_params.get("page", 1)),
                "next_url": self.get_next_link(),
                "previous_url": self.get_previous_link(),
                "results": data,
            }
        )