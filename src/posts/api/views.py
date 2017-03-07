from django.db.models import Q
from rest_framework.filters import (
		SearchFilter,
		OrderingFilter,
	)

from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	UpdateAPIView,
	DestroyAPIView, 
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	)
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination
from .permissions import IsOwnerOrReadonly
from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from posts.models import Post

from .serializers import PostListSerializer, PostDetailSerializer, PostCreateUpdateSerializer


class PostCreateAPIView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer
	permission_classes = [IsAuthenticated, IsAdminUser, ]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
		
	

class PostListAPIView(ListAPIView):
	
	serializer_class = PostListSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	filter_fields = ['title', 'content' , 'user__first_name']
	pagination_class = PostPageNumberPagination

	def get_queryset(self, *args, **kwargs):
		queryset_list = Post.objects.all()
		query = self.request.GET.get("q")
		if query:
			queryset_list = queryset_list.filter(
				Q(title__icontains=query)|
				Q(content__icontains=query)|
				Q(user__first_name__icontains=query) |
				Q(user__last_name__icontains=query)
				).distinct()
		return queryset_list




class PostUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer
	lookup_field = "slug"
	# lookup_url_kwarg
	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadonly]


	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
	

class PostDeleteAPIView(DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = "slug"
	# lookup_url_kwarg
	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadonly]



class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = "slug"
	# lookup_url_kwarg

