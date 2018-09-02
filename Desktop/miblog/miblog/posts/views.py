from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .forms import PostForm
from .models import Post

# Create your views here.
def post_create(request):
	#Llenar Formulario
	form = PostForm(request.POST or None, request.FILES or None)
	#if request.method == "POST":
		#print(request.POST.get("titulo"))
		#print(request.POST.get("contenido"))
		#Validar Formulario
	if (form.is_valid()):
		instance = form.save(commit=False)
		# mas codigo, cambiando el modo de guardar
		instance.save()
		messages.success(request, "Tu post ha sido creado correctamente.")
		return HttpResponseRedirect(instance.get_absolute_url())
	context_data = {
        "form" : form
	}
	return render(request, "post_form.html", context_data)

def post_details(request, id=None):
	#instance = Post.objects.get(id=3)
	instance = get_object_or_404(Post, id=id)
	context_data = {
        "titulo" : instance.titulo,
        "instance" : instance,
	}
	return render(request, "post_details.html", context_data)

def post_list(request):
	queryset_list = Post.objects.all()
	#Fase de Paginacion
	paginator = Paginator(queryset_list, 10)
	page_request_var = "list"
	page = request.GET.get(page_request_var)
	queryset = paginator.get_page(page)
	# Fin de Paginacion

	context_data = {
        "titulo" : "List",
        "Object_List" : queryset,
        "page_request_var" : page_request_var,
	}
	return render(request, "post_list.html", context_data)

def post_update(request, id=None):
	#Obtener informacion del Post
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if (form.is_valid()):
		#Guardar los documentos y almacenarlo en la BBDD
		instance = form.save(commit=False)
		instance.save()
		#Link para dirigir a la pricipal
		messages.success(request, "Tu <a href='#'> post </a> ha sido modificado correctamente.", extra_tags="html_safe")
		return HttpResponseRedirect(instance.get_absolute_url())
	context_data = {
        "titulo" : instance.titulo,
        "instance" : instance,
        "form" : form,
	}
	return render(request, "post_form.html", context_data)

def post_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Tu post ha sido eliminado correctamente.")
	return redirect("list")