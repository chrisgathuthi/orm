from django.core.management.base import BaseCommand
from faker import Faker
from query.models import Blog, User

class Command(BaseCommand):

    help = "seeding blog instances"

    def handle(self, *args, **kwargs):

        fake = Faker()
        user = User.objects.first()

        for _ in range(50):
            Blog.objects.create(
                author = user,
                title= fake.text(max_nb_chars=30),
                content=fake.paragraph(nb_sentences=25, variable_nb_sentences=True)
            )
        print("complete")
