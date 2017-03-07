from rest_framework.permissions import BasePermission


class IsOwnerOrReadonly(BasePermission):
	message = 'You must be the owner of this object.'

	def has_permission(self, request, view):
		my_method = ['GET', 'PUT']
		if request.method in my_method:
			return True
		return False

	def has_object_permission(self, request, view, obj):
		return obj.user == request.user

