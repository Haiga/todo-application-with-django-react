from django.db import models
# from django.core.validators import MaxValueValidator

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    # models.DecimalField(validators=[MaxValueValidator(100)])

    def _str_(self):
        return self.title
