from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.models import Question, Author, Tag, Answer, questionLike, answerLike
import random
from random import choice
from random import choices
from faker import Faker


f = Faker()



class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--authors', type=int)
        parser.add_argument('--questions', type=int)
        parser.add_argument('--answers', type=int)
        parser.add_argument('--tags', type=int)
        parser.add_argument('--questionLikes', type=int)
        parser.add_argument('--answerLikes', type=int)

    

    def fill_tags(self, cnt):
        if cnt == None:
            return None
        for i in range(cnt):
            t = Tag()
            t.name = f.word()
            t.save()





    def fill_authors(self, cnt):
        if cnt == None:
            return None
        for i in range(cnt):
            u = User(username=f.name())
            u.save()
            Author.objects.create(
                user=u
            )




    def fill_questions(self, cnt):
        if cnt == None:
            return None
        author_ids = list(
            Author.objects.values_list(
                'id', flat=True
            )
        )
        tag_ids = list(
            Tag.objects.values_list(
                'id', flat=True
            )
        )
        Tags = Tag.objects.all()
        for i in range(cnt):
            quest = Question.objects.create(
                author=Author.objects.get(pk = choice(author_ids)) ,
                text='. '.join(f.sentences(f.random_int(min=2, max=5))),
                title=f.sentence()[:128],
                create_date=f.date(),
            )
            tag_ch = choices(Tags,  k=random.randint(1,2))
            for t in tag_ch:
                quest.tags.add(t)



    def fill_answers(self, cnt):
        if cnt == None:
            return None
        author_ids = list(
            Author.objects.values_list(
                'id', flat=True
            )
        )
        question_ids = list(
            Question.objects.values_list(
                'id', flat=True
            )
        )
        for i in range(cnt):
            Answer.objects.create(
                author=Author.objects.get(pk = choice(author_ids)),
                text='. '.join(f.sentences(f.random_int(min=1, max=4))),
                create_date=f.date(),
                question=Question.objects.get(pk = choice(question_ids)),
            )


    def fill_questionLikes(self, cnt):
        if cnt == None:
            return None
        author_ids = list(
            Author.objects.values_list(
                'id', flat=True
            )
        )
        question_ids = list(
            Question.objects.values_list(
                'id', flat=True
            )
        )        
        for i in range(cnt):
            questionLike.objects.create(
                author=Author.objects.get(pk = choice(author_ids)),
                current_state = f.pybool(),
                question=Question.objects.get(pk = choice(question_ids)),
            )


    def fill_answerLikes(self, cnt):
            if cnt == None:
                return None
            author_ids = list(
                Author.objects.values_list(
                    'id', flat=True
                )
            )
            answer_ids = list(
                Answer.objects.values_list(
                    'id', flat=True
                )
            )        
            for i in range(cnt):
                answerLike.objects.create(
                    author=Author.objects.get(pk = choice(author_ids)),
                    current_state = f.pybool(),
                    answer=Answer.objects.get(pk = choice(answer_ids)),
                )


    def handle(self, *args, **options):
        self.fill_authors(options.get('authors', 0))
        self.fill_questions(options.get('questions', 0))
        self.fill_tags(options.get('tags', 0))
        self.fill_answers(options.get('answers', 0))
        self.fill_questionLikes(options.get('questionLikes', 0))
        self.fill_answerLikes(options.get('answerLikes', 0))

