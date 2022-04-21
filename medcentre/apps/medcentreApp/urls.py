from django.urls import path

from . import views

app_name = "medcentreApp"
urlpatterns = [
    path('', views.index, name = '_index_'),
    path('<int:article_id>/', views.det, name='det'),
        path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment')
]