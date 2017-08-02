# Django
from django.conf.urls import url, include

# Third-Party
from rest_framework import routers

# Local Django
from tasks.api_views import TaskViewSet
from users.api_views import UserViewSet

router_V1 = routers.DefaultRouter()

LIST_V1 = [
    (r'tasks', TaskViewSet),
    (r'users', UserViewSet)
]


for router in LIST_V1:
    router_V1.register(router[0], router[1])


urlpatterns = [
    url(r'v1/', include(router_V1.urls, namespace='v1')),
]
