from functools import wraps
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group

def permission_required(perm, group_name, login_url=None):
    def check_perms(user):
        if user.has_perm(perm):
            return True
        try:
            group = Group.objects.get(name=group_name)
            return user.groups.filter(name=group_name).exists() and group.permissions.filter(codename=perm).exists()
        except Group.DoesNotExist:
            return False

    return user_passes_test(check_perms, login_url=login_url)