from django.shortcuts import render, get_object_or_404
from .models import Standings, Post
from django.views.generic import ListView, DetailView
from django.views import View
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
class StartingPageView(ListView):
    template_name="premier/index.html"
    model= Standings
    #context_object_name = "table"

    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context["table"] = Standings.objects.all()
         context["featured"] = Post.objects.all().order_by("-date")[:3]
         return context

class AllPostsView(ListView):
    template_name = "premier/news.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

class SinglePostView(DetailView):
    #template_name = "premier/post-detail.html"
    #model = Post


    def get(self,request,slug):
        post=Post.objects.get(slug=slug) 
        context={
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(), 
            "comments": post.comments.all().order_by("-id"), 
        }
        return render(request,"premier/post-detail.html", context)


    def post(self,request,slug):
        comment_form=CommentForm(request.POST)
        post=Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment= comment_form.save(commit=False)
            comment.post=post 
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page",args=[slug]))
        
        context={
            "post":post,
            "post_tags":post.tags.all(),
            "comment_form":comment_form,
            "comments":post.comments.all().order_by("-id"),
        }
        return render(request,"premier/post-detail.html", context)


class ClubsView(ListView):
    template_name = "premier/clubs.html"
    model = Standings
    ordering = ["club"]
    context_object_name = "list"


class SingleClubView(DetailView):
    #template_name = "premier/post-detail.html"
    #model = Post

    def get(self, request, standings_slug):
        club=Standings.objects.get(standings_slug=standings_slug) 
        context={
            "post": club,
            "saved_for_later": self.is_favorite(request, club.id) 
        }
        return render(request,"premier/club-detail.html", context)


    def is_favorite(self, request, post_id): 
        favorites = request.session.get("favorites")
        if favorites is not None: 
            is_favorite = post_id in favorites
        else:
            is_favorite = False
        return is_favorite



class ReadLaterView(View):
    def get(self,request):
        favorites=request.session.get("favorites")
        context={}
        if favorites is None or len(favorites)==0: 
            context["list"]=[]
            context["has_post"]=False
        else:
            posts=Standings.objects.filter(id__in=favorites)
            context["list"]=posts
            context["has_posts"]=True
        return render(request,"premier/favorite-clubs.html",context)


    def post(self,request):
        favorites=request.session.get("favorites")
        if favorites is None: 
            favorites=[]

        post_id= int(request.POST["post_id"])
        if post_id not in favorites: 
            favorites.append(post_id)
        else:
            favorites.remove(post_id)
        request.session["favorites"]=favorites 
        return HttpResponseRedirect("clubs") 
