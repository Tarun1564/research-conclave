from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import UserProfile


class Command(BaseCommand):
    help = "Create User"

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, required=True)
        parser.add_argument('--password', type=str, required=True)
        parser.add_argument('--role', type=str, choices=['evaluator', 'dean'], required=True)
        parser.add_argument('--branch', type=str, required=True)
    def handle(self, *args, **options):

        username = options['username']
        password = options['password']
        role = options['role']
        branch = options['branch']

        user = User.objects.create_user(
            username=username,
            password=password
        )

        UserProfile.objects.create(
            user=user,
            role=role,
            branch=branch
        )

        self.stdout.write(self.style.SUCCESS(f"{role} '{username}' created successfully"))