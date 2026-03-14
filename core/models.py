from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
class Uploads(models.Model):
    file = CloudinaryField(resource_type='raw', folder='research_papers/')
    branch = models.CharField(max_length=100)
    roll_number=models.CharField(max_length=50,unique=True,blank=True,null=True)
    abstract = models.FloatField(null=True, blank=True)
    research_methodology = models.FloatField(null=True, blank=True)
    results = models.FloatField(null=True, blank=True)
    formatting = models.FloatField(null=True, blank=True)
    conclusion = models.FloatField(null=True, blank=True)
    overall_score = models.FloatField(null=True, blank=True)
    is_top = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.roll_number}-{self.file.url}"

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('dean', 'Dean'),
        ('evaluator', 'evaluator'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    branch = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return f"{self.user.username} - {self.role}"
class Evaluator(models.Model):
    papers = models.ManyToManyField(Uploads, related_name='evaluations')
    evaluator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=50,unique=True, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True)
    evaluated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return   f"{self.name}"