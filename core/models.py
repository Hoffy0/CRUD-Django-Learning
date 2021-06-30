from django.db import models
from django.contrib.auth.models import User

## Crear el modelo de la tarea en python para despues migrarla a la base de datos
class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank= True)
    title = models.CharField(max_length=50)
    desc = models.TextField(null = True, blank = True)
    isComplete = models.BooleanField(default=False)
    createAt =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['isComplete']
