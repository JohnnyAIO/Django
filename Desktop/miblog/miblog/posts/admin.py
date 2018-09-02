from django.contrib import admin
from .models import Post
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
	list_display = ["titulo", "actualizado", "timesmap"]
	list_display_links = ["actualizado"]
	list_filter = ["timesmap"]
	list_editable = ["titulo"]
	search_fields = ["titulo", "contenido"]

	class Meta:
		model = Post
admin.site.register(Post, PostModelAdmin)
