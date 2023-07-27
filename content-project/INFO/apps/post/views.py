# from django.shortcuts import render
from typing import Any, Dict
from .models import Post, Comentario
from .forms import ComentarioForm
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse

#Vista basada en funciones
# def posts(request):
#     posts =Post.objects.all()
#     print(posts)
#     return render(request, "posts.html", {"posts" : posts})

#Vista basada en clases
class PostListView(ListView):
    model = Post
    template_name = "posts/posts.html"
    context_object_name = "posts"

class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_individual.html"
    context_object_name = "posts"
    pk_url_kwarg = "id"
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["post"] = Post.objects
        context["form"] = ComentarioForm()
        context["comentarios"] = Comentario.objects.filter(posts_id=self.kwargs["id"])
        return context
    
    def post(self, request, *args, **kwargs): 
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.posts_id = self.kwargs["id"]
            comentario.save()
            return redirect("apps.post:post_individual", id=self.kwargs["id"])
        else:
            context = self.get_context_data(**kwargs)
            context["form"] = form
            return self.render_to_response(context)
        
class ComentarioCreateView(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = "comentario/agregarComentario.html"
    success_url = "comentario/comentarios"

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.posts_id = self.kwargs["posts_id"]
        return super().form_valid(form)


# Create your views here.
