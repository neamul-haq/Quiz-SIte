from django.contrib import admin
from .models import Quiz, Question, Option, UserAnswer, UserQuizHistory, Rating, QuizRating

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(UserAnswer)
admin.site.register(UserQuizHistory)
admin.site.register(Rating)
admin.site.register(QuizRating)

# class OptionInline(admin.TabularInline):  # Inline for Option model
#     model = Option

# class QuestionAdmin(admin.ModelAdmin):
#     inlines = [OptionInline]

# admin.site.register(QuestionAdmin)  # Register the QuestionAdmin class, not an instance