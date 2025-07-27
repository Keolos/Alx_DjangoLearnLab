from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver

@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    if sender.name == 'bookshelf':  # Only run for this app
        # Create groups
        editors_group, _ = Group.objects.get_or_create(name='Editors')
        viewers_group, _ = Group.objects.get_or_create(name='Viewers')
        admins_group, _ = Group.objects.get_or_create(name='Admins')

        # Get permissions
        can_view = Permission.objects.get(codename='can_view')
        can_create = Permission.objects.get(codename='can_create')
        can_edit = Permission.objects.get(codename='can_edit')
        can_delete = Permission.objects.get(codename='can_delete')

        # Assign permissions
        editors_group.permissions.set([can_view, can_create, can_edit])
        viewers_group.permissions.set([can_view])
        admins_group.permissions.set([can_view, can_create, can_edit, can_delete])
