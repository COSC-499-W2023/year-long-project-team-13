from .models import Notification

def notifications(request):
    if request.user.is_authenticated:
        unread_notifications_count = Notification.objects.filter(user=request.user, is_read=False).count()
        return {'unread_notifications_count': unread_notifications_count}
    else:
        return {}