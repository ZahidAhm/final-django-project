from django.contrib import admin
# import new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice

# Registering QuestionInline and ChoiceInline classes here


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 5


# Registering models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# Question and Choice models
class Question(models.Model):
    # Foreign key to lesson
    # question text
    # question grade/mark
    lessor=models.ForeignKey(Lesson, on_delete=models.CASCADE)
    text = models.CharField(max_length=150)
    grade = models.FloatField()
    # A sample model method to calculate if learner get the score of the question
    def is_get_score(self, selected_ids):
        all_answers = self.choice_set.filter(is_correct=True).count()
        selected_correct = self.choice_set.filter(is_correct=True, id__in=selected_ids).count()
        if all_answers == selected_correct:
            return True
        else:
            return False
    

    # Model method to calculate if learner get the score of the question
    def is_get_score(self, selected_ids):
        all_answers = self.choice_set.filter(is_correct=True).count()
        selected_correct = self.choice_set.filter(is_correct=True, id__in=selected_ids).count()
        if all_answers == selected_correct:
            return True
        else:
            return False


#  Choice Model:

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=250, default="question text")
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return self.content + (' :is correct' if self.is_correct else ' :not correct')



admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
