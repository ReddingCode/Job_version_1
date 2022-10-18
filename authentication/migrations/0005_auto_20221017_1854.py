# Generated by Django 3.2.16 on 2022-10-17 16:54

from django.db import migrations


def create_groups(apps, schema_migration):
    User = apps.get_model('authentication', 'User')
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    add_worker = Permission.objects.get(codename='add_worker')
    change_worker = Permission.objects.get(codename='change_worker')
    delete_worker = Permission.objects.get(codename='delete_worker')
    view_worker = Permission.objects.get(codename='view_worker')

    workers_permissions = [
        add_worker,
        change_worker,
        delete_worker,
        view_worker,
    ]

    workers = Group(name='workers')
    workers.save()
    workers.permissions.set(workers_permissions)

    subscribers = Group(name='subscribers')
    subscribers.save()
    subscribers.permissions.add(view_worker)

    for user in User.objects.all():
        if user.role == 'WORKER':
            workers.user_set.add(user)
        if user.role == 'SUBSCRIBER':
            subscribers.user_set.add(user)

class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_user_profile_photo'),
    ]

    operations = [
        migrations.RunPython(create_groups)
    ]
