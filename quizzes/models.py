from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg

class Quiz(models.Model):
    CATEGORY_CHOICES = (
        ('C', 'C'),
        ('CPP', 'CPP'),
        ('Python', 'Python'),
        ('Java', 'Java'),
        ('PHP', 'PHP'),
        # Add more choices as needed
    )

    title = models.CharField(max_length=255)
    description = models.TextField(default="Default description")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    # time_limit = models.PositiveIntegerField(null=True, blank=True)
    time_limit = models.PositiveIntegerField(default=0)  # 0 means no time limit
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    def __str__(self):
        return self.title
    
    def update_average_rating(self):
        average_rating = self.rating_set.aggregate(Avg('rating'))['rating__avg']
        if average_rating is not None:
            self.average_rating = round(average_rating, 2)
        else:
            self.average_rating = 0.00
        self.save()


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()
    
    def __str__(self) -> str:
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.text

class UserQuizHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)

class QuizRating(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 8)])
    
class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - Q{self.question.id}"
    

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} - {self.rating}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.quiz.update_average_rating()


