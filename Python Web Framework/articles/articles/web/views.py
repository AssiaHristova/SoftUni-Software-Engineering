from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, ListView
from django.views.generic.detail import SingleObjectMixin

from articles.web.models import Article, Source


class CreateArticleView(CreateView):
    model = Article
    fields = '__all__'
    template_name = 'web/create-article.html'
    success_url = reverse_lazy('list articles')


class ListArticlesView(ListView):
    model = Article
    template_name = 'web/list-articles.html'


class CreateSourceView(CreateView):
    model = Source
    fields = '__all__'
    template_name = 'web/create-source.html'
 #   success_url = reverse_lazy('list sources')

    def get_success_url(self):
        return reverse('source details',
                       kwargs={'pk': self.object.id}
                       )


class SourceDetailsView(SingleObjectMixin, ListView):
    model = Source
    template_name = 'web/source-details.html'
    object = None
    paginate_by = 1

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Source.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['source'] = self.object
        return context

    def get_queryset(self):
        return self.object.article_set.all()


class ListSourcesView(ListView):
    model = Source
    template_name = 'web/list-sources.html'

