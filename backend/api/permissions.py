from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': [],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
    
    def has_permission(self, request, view):
        if not request.user.is_staff:
            return False
        
        return super().has_permission(request, view)
    
    # def has_permission(self, request, view):
    #     user = request.user
    #     print(user.get_all_permissions())

    #     if user.is_staff:
    #         if user.has_perm("classes.add_class"):
    #             return True
    #         if user.has_perm("classes.view_class"):
    #             return True
    #         if user.has_perm("classes.change_class"):
    #             return True
    #         if user.has_perm("classes.delete_class"):
    #             return True
            
    #         return False
        
    #     return False 

# class IsOwnerOrReadOnly(permissions.BasePermission):
#     """
#     Object-level permission to only allow owners of an object to edit it.
#     Assumes the model instance has an `owner` attribute.
#     """

#     def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request,
#         # so we'll always allow GET, HEAD or OPTIONS requests.
#         if request.method in permissions.SAFE_METHODS:
#             return True

#         # Instance must have an attribute named `owner`.
#         return obj.owner == request.users