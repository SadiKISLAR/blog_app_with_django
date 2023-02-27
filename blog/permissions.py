from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    massage = "You aren't the owner of this post"

    def has_object_permission(self, request, obj):
        return obj.author == request.user