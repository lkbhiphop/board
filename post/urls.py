from django.urls import path
from . import views
# 이 views는 app내에 있는 views를 사용한다.
app_name = 'post'
urlpatterns = [
    path('',views.list, name = 'list'),
    path('create/',views.create, name = 'create'),
    path('<int:id>/detail/',views.detail, name = 'detail')
    ]