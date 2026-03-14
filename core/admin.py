from django.contrib import admin
from .models import Uploads, UserProfile, Evaluator
admin.site.site_header = "Research Conclave Admin"
admin.site.site_title = "Research Conclave Admin Portal"
admin.site.index_title = "Welcome to Research Conclave Admin Portal"
admin.site.register(Uploads)
admin.site.register(UserProfile)
admin.site.register(Evaluator)