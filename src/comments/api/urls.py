from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import (
		CommentListAPIView,
	)

urlpatterns = [
	url(r'^$', CommentListAPIView.as_view(), name='comment-list'),
]

