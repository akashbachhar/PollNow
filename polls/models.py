from django.db import models


class QuestionModel(models.Model):
    question_text = models.TextField()
    choice_text1 = models.CharField(max_length=200)
    choice_text2 = models.CharField(max_length=200)
    choice_text3 = models.CharField(max_length=200)
    choice_vote1 = models.IntegerField(default=0)
    choice_vote2 = models.IntegerField(default=0)
    choice_vote3 = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text
