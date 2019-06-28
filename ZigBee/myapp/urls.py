from django.conf.urls import url, include
from rest_framework import routers
from myapp import views

app_name = '[myapp]'

routers = routers.DefaultRouter()

routers.register(r'user', views.UserSet)
routers.register(r'foods', views.FoodsSet)
routers.register(r'message', views.MessageSet)

urlpatterns = [
    url(r'^', include(routers.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]