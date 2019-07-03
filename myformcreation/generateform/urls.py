from django.conf.urls import url
from generateform import views


urlpatterns = [
    url(r'^create/', views.form_view, name='form page'),
]
