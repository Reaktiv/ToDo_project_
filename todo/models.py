from django.db import models


class ToDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # user = models.ForeignKey(on_delete=models.CASCADE)


    def __str__(self):
        return self.title


