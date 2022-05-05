from .models import ToDoItem, ToDoList
from django import forms


class ToDoItemForm(forms.ModelForm):

    class Meta:
        model = ToDoItem

        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ToDoItemForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ToDoListForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
