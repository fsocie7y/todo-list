from django.urls import path

from todo_list.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    change_task_status,
    TagCreateView,
    TagsListView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="tasks"),
    path("create-task/", TaskCreateView.as_view(), name="create_task"),
    path("tasks/<int:pk>/change/", change_task_status, name="change-status"),
    path("tasks/<int:pk>/update/",
         TaskUpdateView.as_view(),
         name="update-task"),
    path("tasks/<int:pk>/delete/",
         TaskDeleteView.as_view(),
         name="delete-task"),
    path("create-tag/", TagCreateView.as_view(), name="create_tag"),
    path("tags/", TagsListView.as_view(), name="tags"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="update-tag"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="delete-tag"),

]

app_name = "todo_list"
