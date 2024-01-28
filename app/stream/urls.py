from . import views
from . views import (
    VideoDetailView,
    UserVideoListView,
    VideoCreateView,
    GeneralVideoListView,
    VideoUpdateView,
    VideoDeleteView,
    FriendRequset,
)
from django.urls import path
from stream import views as stream_views
from django.contrib.auth import views as auth_views



app_name = "stream"

urlpatterns = [

    path('video/<int:pk>/', VideoDetailView.as_view(), name="video-detail"),
    path('video/<int:pk>/update/', VideoUpdateView.as_view(), name="video-update"),
    path('video/<int:pk>/delete/', VideoDeleteView.as_view(), name="video-delete"),
    path('user/<str:username>', UserVideoListView.as_view(), name="user-videos"),
    path('video/new/',VideoCreateView.as_view(), name="video-create"),
    path('search',views.search,name="search"),
    path('',views.home,name="home"),
    path('video',GeneralVideoListView.as_view(), name="video-list"),
    # Use friendRequest if it is complete instead of contact
    # path('contact',views.contact,name="contact"),
    path('contact',views.friendRequest,name="contact"),
    # path('contact',FriendRequset.as_view(),name="contact"),

    path('request-video',views.request_video,name="request-video"),

    path('profile',stream_views.profile, name="profile"),
    path('register/',stream_views.register, name="register"),
    path('login', auth_views.LoginView.as_view(template_name='stream/login.html'), name="login"),
    path('logout',auth_views.LogoutView.as_view(template_name='stream/logout.html'), name="logout"),
    path('setting',auth_views.LoginView.as_view(template_name='stream/settings.html'), name="setting"),
    path('theme',auth_views.LoginView.as_view(template_name='stream/theme.html'), name="theme"),
    path('notifications',stream_views.notifications, name="notifications"),
]
