from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "You aren't the owner of this post"

    def has_object_permission(self, request, view, obj):
        return obj.author.id == request.user.id