from rest_framework.pagination import (
    BasePagination,
    PageNumberPagination,
    Response,
)


class CatsPagination(PageNumberPagination):
    page_size = 20


class CatsCustomPagination(PageNumberPagination):
    # display_page_controls = 20
    page_size = 20

    # def paginate_queryset(self, queryset, request, view=None):
    #     return queryset

    def get_paginated_response(self, data):
        return Response(
            {
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link(),
                },
                'count': self.page.paginator.count,
                'result': data,
            }
        )
