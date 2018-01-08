
from django.db import models

from django_tex.models import TeXTemplateFile

class TemplateFile(TeXTemplateFile):
    pass

class Entry(models.Model):

    date = models.DateField()