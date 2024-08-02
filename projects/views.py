from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from . import models
from . import forms



class ProjectListView(ListView):
    model = models.Project
    template_name = 'project/list.html'
    paginate_by = 6
    def get_queryset(self):
        query_set =super().get_queryset()
        where = {}
        q = self.request.GET.get('q', None)
        if q:
            where['title__icontains'] = q
            return query_set.filter(**where)
class ProjectCreateView(CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('project_list')
# Create your views here.
class ProjectUpdateView(UpdateView):
    model = models.Project
    form_class = forms.ProjectupdateForm
    template_name = 'project/update.html'

    def get_success_url(self):
        return reverse_lazy('project_update', args=[self.object.id])


class ProjectDeleteView(DeleteView):
    model = models.Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('project_list')

class TaskCreateView(CreateView):
    model = models.Task
    fields = ['project', 'description']
    http_method_names = ['post']
    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])


class TaskUpdateView(UpdateView):
    model = models.Task
    fields = ['is completed']
    http_method_names = ['post']
    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])

class TaskDeleteView(CreateView):
    model = models.Task

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])
