from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsVerifiedForActions(BasePermission):
    """
    Allows any authenticated user to VIEW data (GET, HEAD, OPTIONS)
    regardless of verification status.

    Blocks WRITE actions (POST, PUT, PATCH, DELETE) — like booking a
    pickup, sending money, or filing a complaint — until the user's
    profile is verified by the operator admin.
    """
    message = "Your profile is under verification. This action will be available once approved."

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        # Always allow read-only access (viewing screens, browsing data)
        if request.method in SAFE_METHODS:
            return True

        # Only 'user' role has a UserProfile with is_verified — check it
        if request.user.base_role == 'user':
            try:
                return request.user.user_profile.is_verified
            except AttributeError:
                return False

        # For operator/operatoradmin roles, this permission isn't relevant
        # here — leave that check to a separate permission class later.
        return True


class IsOperatorRole(BasePermission):
    message = "Operator privileges required."

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.base_role == 'operator'
        )


class IsStaffRole(BasePermission):
    message = "Operator or operator admin privileges required."

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.base_role in ('operator', 'operatoradmin')
        )


class IsApprovedStaff(BasePermission):
    message = "Your account is still pending approval. Wait for the admin to approve your onboarding."

    def has_permission(self, request, view):
        if not (
            request.user
            and request.user.is_authenticated
            and request.user.base_role in ('operator', 'operatoradmin')
        ):
            return False
        profile = (
            request.user.operatoradmin_profile
            if request.user.base_role == 'operatoradmin'
            else getattr(request.user, 'operator_profile', None)
        )
        return bool(profile and profile.is_verified)


class IsOperatorAdminOrSuperAdmin(BasePermission):
    message = "Operator admin or super admin privileges required."

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.base_role in ('operatoradmin', 'superadmin')
        )


class IsSuperAdminRole(BasePermission):
    message = "Super admin privileges required."

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.base_role == 'superadmin'
        )