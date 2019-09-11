from django.contrib import admin
from django.urls import path
from bboard.views import index, by_rubric
from bboard.views import BbCreateView


urlpatterns = [
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('add/', BbCreateView.as_view(),name='add'),
]
