# Django
from django.conf.urls import url, include

# Third-Party
from rest_framework import routers

# Local Django
from users.api_views import UserViewSet
from tasks.api_views import TaskViewSet, ReminderViewSet

router_V1 = routers.DefaultRouter()

LIST_V1 = [
    (r'users', UserViewSet),
    (r'tasks', TaskViewSet),
    (r'reminders', ReminderViewSet)
]


for router in LIST_V1:
    router_V1.register(router[0], router[1])


urlpatterns = [
    url(r'v1/', include(router_V1.urls, namespace='v1')),
]
