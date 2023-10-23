from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin


class RecipeInline(admin.StackedInline):
    model = models.Recipe
    extra = 1 #количество рецептов в меню добавления поста(по дефолту было 3)


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'create_at', 'id']
    prepopulated_fields = {"slug": ("title",)}
    inlines = [RecipeInline] #присоединием к админке возможность в добавлении постаа выбор рецепта
    save_as = True
    save_on_top = True
@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'prep_time', 'cook_time', 'post']


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)

admin.site.register(models.Comment)
