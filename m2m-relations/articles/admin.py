from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Tag

class ScopeInlineFormset(BaseInlineFormSet):
   def clean(self):
      if len(self.forms) == 0:
         raise ValidationError('Не определены рубрики')

      count_main = 0
      for form in self.forms:
         # В form.cleaned_data будет словарь с данными
         # каждой отдельной формы, которые вы можете проверить
         if form.cleaned_data['is_main']:
            count_main += 1
         if count_main > 1:
            raise ValidationError('Главная рубрика отмечена более одного раза!')
         # вызовом исключения ValidationError можно указать админке о наличие ошибки
         # таким образом объект не будет сохранен,
         # а пользователю выведется соответствующее сообщение об ошибке
         # raise ValidationError('Тут всегда ошибка')
      return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
   model = Scope
   formset = ScopeInlineFormset
   extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
   inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']