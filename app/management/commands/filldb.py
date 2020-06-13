from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.models import Question, Author, Tag
from random import choice
# from django_faker import Faker
from faker import Faker
# from factory.faker import faker

f = Faker()
# populator = Faker.getPopulator()


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--authors', type=int)
        parser.add_argument('--questions', type=int)
        parser.add_argument('--answers', type=int)
        parser.add_argument('--tags', type=int)

    
    def fill_tags(self, cnt):
        i = 0
        for i in range(cnt):
            t = Tag()
            t.name = f.name()
            t.save()




    def fill_authors(self, cnt):
        # populator.addEntity(Author, cnt)
        i = 0
        while i < cnt:
            u = User(username=f.name())
            u.save()
            Author.objects.create(
                user=u
            )
            i = i + 1
        # cnt = int(cnt)
        # for i in range(cnt):
        #     u = User(username=f.name())
        #     u.save()
        #     Author.objects.create(
        #         user=u
        #     )




    def fill_questions(self, cnt):
        author_ids = list(
            Author.objects.values_list(
                'id', flat=True
            )
        )
        i = 0
        cnt = int(cnt)
        for i in range(cnt):
            Question.objects.create(
                author=choice(author_ids),
                content='. '.join(f.sentences(f.random_int(min=2, max=5))),
                title=f.sentence()[:128],
            )



    def handle(self, *args, **options):
        self.fill_authors(options.get('authors', 0))
        self.fill_questions(options.get('questions', 0))
        self.fill_tags(options.get('tags', 0))
        # self.fill_answers(answers_cnt)
