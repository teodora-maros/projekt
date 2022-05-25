from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.StartingPageView.as_view(), name="standings"),
    path("posts/", views.AllPostsView.as_view(), name="all-posts"),
    path("post/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page"),
    path("clubs", views.ClubsView.as_view(), name="clubs"),
    path("club/<slug:standings_slug>", views.SingleClubView.as_view(), name="club-detail-page"),
    path("favorite-clubs",views.ReadLaterView.as_view(),name="favorite-clubs")
]

urlpatterns += staticfiles_urlpatterns()
