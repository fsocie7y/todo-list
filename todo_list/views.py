from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect

from todo_list.forms import TagForm, TagSearchForm, TaskSearchForm
from todo_list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    queryset = Task.objects.all()
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        content = self.request.GET.get("content", "")

        context["task_search_form"] = TaskSearchForm(initial={
            "content": content
        })

        return context

    def get_queryset(self):
        form = TaskSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                content__icontains=form.cleaned_data["content"]
            )
        return self.queryset


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TagForm
    success_url = reverse_lazy("todo_list:tasks")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TagForm
    success_url = reverse_lazy("todo_list:tasks")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:tasks")


def change_task_status(request, pk: int):
    task = Task.objects.get(pk=pk)

    task.is_done = not task.is_done
    task.save()

    return redirect(reverse_lazy("todo_list:tasks"))


class TagsListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    queryset = Tag.objects.all()
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name", "")

        context["tag_search_form"] = TagSearchForm(initial={
            "name": name
        })

        return context

    def get_queryset(self):
        form = TagSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return self.queryset


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tags")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tags")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tags")
