from django import forms

from books.books_app.models import Book, Author


class BootstrapFormMixin:
    def _init_bootstrap(self):
        for(_, field) in self.fields.items():
            field.widget.attrs={'class': 'form-control'}


class BookForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()
        
    author_name = forms.CharField(max_length=20)

    def save(self, commit=True):
        db_author = Author.objects.filter(name=self.instance.author).first()
        if db_author:
            author = db_author
        else:
            author = Author(name=self.cleaned_data['author_name'])
        author.save()
        self.instance.author = author
        return super().save(commit)

    class Meta:
        model = Book
        fields = ['title', 'pages', 'description', 'author_name']


class StateFilterForm(forms.Form):
    state = forms.BooleanField(
        required=False,
        widget=forms.RadioSelect(
            choices=(
                ('Read', 'read'),
                ('Not read', 'not read'),
                ('All', 'all')
        )))



