from api.views import ListCreateTodo, DetailUpdateDeleteTodo
from django.conf.urls import url


urlpatterns = [
    url(r'^todos/$', ListCreateTodo.as_view(), name="list_create_todo"),
    url(r'^todos/(?P<pk>\d+)/$', DetailUpdateDeleteTodo.as_view(),
        name="detail_update_delete_todo"),
]
