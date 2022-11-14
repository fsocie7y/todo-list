from django.db import models


# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(to=Tag, related_name="tasks")

    class Meta:
        ordering = ["is_done", "-creation"]

    def __str__(self):
        return (
            f"{self.content} (creation - {self.creation}, "
            f"deadline - {self.deadline}), "
            f"is done - {self.is_done}"
        )
