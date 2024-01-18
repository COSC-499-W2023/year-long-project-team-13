from django.shortcuts import render, redirect, get_object_or_404
from . models import VidStream
from . forms import VidUploadForm
from . forms import VidRequestForm
from django.views.generic import DetailView, DeleteView, UpdateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages

class VideoDetailView(DetailView):
    template_name = "stream/video-detail.html"
    model = VidStream

class GeneralVideoListView(ListView):
    model = VidStream
    template_name = 'stream/video-list.html'
    context_object_name = 'videos'
    ordering = ['-upload_date']

def search(request):
    if request.method == "POST":
        query = request.POST.get('title', None)
        if query:
            results = VidStream.objects.filter(title__contains=query)
            return render(request, 'stream/search.html',{'videos':results})

    return render(request, 'stream/search.html')

def home(request):
    return render(request, 'stream/home.html')

def contact(request):
    if request.method == 'POST':
        contact_name = request.POST.get('contact_name')
        user_to_add = User.objects.filter(username=contact_name).first()
        if user_to_add:
            # Add the user to the current user's contacts
            request.user.profile.contacts.add(user_to_add.profile)

            # Add a notification to the user being added
            user_to_add.profile.notifications += f"You have received a contact request from {request.user.username}.\n"
            user_to_add.profile.save()

            messages.success(request, f'Add request to {user_to_add.username} sent successfully!')
        else:
            messages.error(request, f'User {contact_name} not found.')
        return redirect('stream:contact')
    return render(request, 'stream/contact.html')

def request_video(request):
    if request.method == "POST":
        form = VidRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stream:home')
    else:
        form = VidRequestForm()
        return render(request, 'stream/request-video.html', {'form':form})


class VideoCreateView(LoginRequiredMixin   ,CreateView):
    model = VidStream
    success_url = "/"
    template_name = 'stream/post-video.html'
    fields = ['title', 'description','video']


    #this is to make sure that the logged in user is the one to upload the content
    def form_valid(self, form):
        form.instance.streamer = self.request.user
        return super().form_valid(form)


class VideoUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = VidStream
    template_name = 'stream/post-video.html'
    success_url = "/"
    fields = ['title','description','video']


    #this is to make sure that the logged in user is the one to upload the content
    def form_valid(self, form):
        form.instance.streamer = self.request.user
        return super().form_valid(form)
    #this function prevents other people from updating your videos
    def test_func(self):
        video = self.get_object()
        if self.request.user == video.streamer:
            return True
        return False




class VideoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "stream/video-confirm-delete.html"
    success_url = "/"
    model = VidStream

    def test_func(self):
        video = self.get_object()
        if self.request.user == video.streamer:
            return True
        return False



class UserVideoListView(ListView):
    model = VidStream
    template_name = "stream/user_videos.html"
    context_object_name = 'videos'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return VidStream.objects.filter(streamer=user).order_by('-upload_date')
