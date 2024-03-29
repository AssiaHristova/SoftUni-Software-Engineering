from django import template

from templates_advanced.todos.models import Todo

register = template.Library()


@register.simple_tag()
def todos_count():
    return Todo.objects.count()


@register.inclusion_tag('shared/template_tags/todos_preview.html')
def todos_preview():
    return {'count': Todo.objects.count()}

