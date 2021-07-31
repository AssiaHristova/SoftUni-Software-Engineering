from django.urls import path
from articles.web.views import ListArticlesView, CreateArticleView, SourceDetailsView, CreateSourceView, ListSourcesView

urlpatterns = [
    path('', ListArticlesView.as_view(), name='list articles'),
    path('article/create/', CreateArticleView.as_view(), name='create article'),
    path('sources/', ListSourcesView.as_view(), name='list sources'),
    path('source/create/', CreateSourceView.as_view(), name='create source'),
    path('source/details/<int:pk>', SourceDetailsView.as_view(), name='source details'),
]
