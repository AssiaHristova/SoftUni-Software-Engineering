from django.contrib import admin

from to_do.to_do_app.models import ToDo
from to_do.to_do_app.models.to_do_models import Category, Person


class ToDoAdmin(admin.ModelAdmin):
    list_display = ['text', 'owner']
    sortable_by = 'text'
    list_filter = ['owner']

  #  def has_change_permission(self, request, obj=None):
   #     return False


admin.site.register(ToDo, ToDoAdmin)
admin.site.register(Person)
admin.site.register(Category)
