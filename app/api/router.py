from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from app.api import views

router = DefaultRouter()

urlpatterns = [
    url(r'^integration/$', views.run_data_integration, name="run-data-integration"),
    url(r'^geocodage/$', views.run_geocodage, name="run-geocodage"),
]
urlpatterns += router.urls
