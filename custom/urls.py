from django.conf.urls import url
from .views import ActivityView

app_name = "articles"

urlpatterns = [
    url('api-activity/', ActivityView.as_view()),
]