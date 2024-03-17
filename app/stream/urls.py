from . import views
from . views import (
    VideoDetailView,
    UserVideoListView,
    VideoCreateView,
    GeneralVideoListView,
    VideoUpdateView,
    VideoDeleteView,
    FriendRequest,
    PasswordResetView,
    VideoUploadView
)
from django.urls import path
from stream import views as stream_views
from django.contrib.auth import views as auth_views
from django.urls import path




app_name = "stream"

urlpatterns = [

    path('video/<int:pk>/', VideoDetailView.as_view(), name="video-detail"),
    path('video/<int:pk>/update/', VideoUpdateView.as_view(), name="video-update"),
    path('video/<int:pk>/delete/', VideoDeleteView.as_view(), name="video-delete"),
    path('user/<str:username>', UserVideoListView.as_view(), name="user-videos"),
    # VideoCreateView.as_view()
    # stream_views.create_video
    path('video/new/',stream_views.create_video, name="video-create"),
    # VideoUploadView.as_view()
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

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='stream/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='stream/password_reset_done.html'), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
