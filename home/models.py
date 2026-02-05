from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    tech_stack = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class SystemStatus(models.Model):
    active_nodes = models.IntegerField()
    swarm_state = models.CharField(max_length=50)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.swarm_state
