from django.db import models

class RoundRobin(models.Model):
    state = models.IntegerField(default=0)
    limit = models.IntegerField(default=4)
    note = models.CharField(max_length=20)

def get_next(index):
    current = RoundRobin.objects.get(id=index)

    if over_limit(current):
        return reset_robin(current)
    else:
        return increment_state(current)

def over_limit(robin):
    return not (robin.state < robin.limit-1)

def reset_robin(robin):
    robin.state = 0
    robin.save()
    return robin.state

def increment_state(robin):
    robin.state += 1
    robin.save()
    return robin.state
