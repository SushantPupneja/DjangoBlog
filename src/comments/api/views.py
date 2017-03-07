from rest_framework.generics import (
		ListAPIView,
	)

from comments.models import Comment

from .serializers import CommentListAPISerializer

class CommentListAPIView(ListAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentListAPISerializer
