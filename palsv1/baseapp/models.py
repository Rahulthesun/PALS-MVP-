from django.db import models
from django.contrib.auth.models import User

difficulty_choices = (("Beginner",'beginner'),
                      ("Intermediate",'intermediate'),
                      ("Expert",'expert'))
# Create your models here.


class Course(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=200 , choices=difficulty_choices)
    #sub_topics = 
    #completion_level
    description = models.TextField()

    def __str__(self):
        return f"{self.language} {self.difficulty}"

class Subunit(models.Model):
    course = models.ForeignKey(Course , on_delete=models.CASCADE)
    name = models.CharField(max_length=200)  

    def __str__(self):
        return self.name

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subunit = models.ForeignKey(Subunit,on_delete=models.CASCADE)
    question_text = models.TextField()

    def __str__(self):
        return self.question_text[0:10]
    


    


