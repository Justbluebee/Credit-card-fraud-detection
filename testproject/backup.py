from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Perform scheduled backup'

    def handle(self, *args, **options):
        call_command('dbbackup')