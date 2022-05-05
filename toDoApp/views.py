from django.views import generic
from .models import ToDoList, ToDoItem
from django.urls import reverse, reverse_lazy
from .forms import ToDoItemForm, ToDoListForm


class ToDoListView(generic.ListView):
    model = ToDoList
    template_name = 'ToDoApp/index.html'


class ItemListView(generic.ListView):
    model = ToDoItem
    template_name = 'ToDoApp/item-list.html'

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs['list_id'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['todo_list'] = ToDoList.objects.get(id=self.kwargs['list_id'])
        return context


class ListCreateView(generic.CreateView):
    model = ToDoList
    form_class = ToDoListForm
    template_name = 'ToDoApp/todoitem_form.html'

    success_url = reverse_lazy('index')


class ListUpdateView(generic.UpdateView):
    model = ToDoList
    form_class = ToDoListForm
    template_name = 'ToDoApp/todoitem_form.html'
    success_url = reverse_lazy('index')


class ListDeleteView(generic.DeleteView):
    model = ToDoList
    success_url = reverse_lazy('index')


class ItemCreateView(generic.CreateView):
    model = ToDoItem
    form_class = ToDoItemForm

    def get_initial(self):
        initial = super(ItemCreateView, self).get_initial()
        initial['todo_list'] = ToDoList.objects.get(id=self.kwargs['list_id'])
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'add new item to the list'
        return context

    def get_success_url(self):
        return reverse('list', args=[self.object.todo_list_id])


class ItemUpdateView(generic.UpdateView):
    model = ToDoItem
    form_class = ToDoItemForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'edit a item in your list'
        return context

    def get_success_url(self):
        return reverse('list', args=[self.object.todo_list_id])


class ItemDeleteView(generic.DeleteView):
    model = ToDoItem

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['todo_list'] = ToDoList.objects.get(id=self.kwargs['list_id'])
        return context

    def get_success_url(self):
        return reverse_lazy('list', args=[self.object.todo_list_id])


