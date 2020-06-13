from django.contrib import admin
from app.models import Question, Answer, Tag, Author, questionLike, answerLike

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(questionLike)
admin.site.register(answerLike)