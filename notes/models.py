from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note {self.pk}"
    
    class Meta:
        verbose_name_plural = 'notes'