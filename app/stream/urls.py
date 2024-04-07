from . import views
from . views import (
    VideoDetailView,
    UserVideoListView,
    GeneralVideoListView,
    VideoDeleteView,
)
from django.urls import path
from stream import views as stream_views
from django.contrib.auth import views as auth_views

app_name = "stream"

urlpatterns = [

    path('video/<int:pk>/', VideoDetailView.as_view(), name="video-detail"),
    path('video/<int:pk>/record/', stream_views.record_filled_video, name="video-record-filled"),
    path('video/<int:pk>/upload/', stream_views.upload_filled_video, name="video-upload-filled"),
    path('video/<int:pk>/delete/', VideoDeleteView.as_view(), name="video-delete"),
    path('user/<str:username>', UserVideoListView.as_view(), name="user-videos"),
    path('video/new/',stream_views.create_video, name="video-create"),
    path('video/new',stream_views.upload_video, name="video-upload"),
    path('search',views.search,name="search"),
    path('',views.home,name="home"),
    path('video',GeneralVideoListView.as_view(), name="video-list"),
    path('contact',views.friendRequest,name="contact"),
    path('request-video',views.request_video,name="request-video"),

    path('profile',stream_views.profile, name="profile"),
    path('register/',stream_views.register, name="register"),
    path('login', auth_views.LoginView.as_view(template_name='stream/login.html'), name="login"),
    path('logout',auth_views.LogoutView.as_view(template_name='stream/logout.html'), name="logout"),
    path('setting',stream_views.settings, name="setting"),
    path('theme',stream_views.settings, name="theme"),
    path('notifications',stream_views.notifications, name="notifications"),

    path('forget-password/', stream_views.password_reset, name='forget-password'),
    path('security-answer/<str:username>', stream_views.security_answer, name='security-answer'),
    path('password_reset_done/<str:username>', stream_views.password_reset_done, name='password_reset_done'),
]
