from django.db import models
from django.core.exceptions import ValidationError
from django.template import TemplateDoesNotExist
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from django_tex.engine import engine

def validate_template_path(name):
    try: 
        engine.get_template(name)
    except (TemplateDoesNotExist):
        raise ValidationError(_('Template not found.'))

class TeXTemplateFile(models.Model):
    
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255, validators=[validate_template_path,])

    class Meta:
        abstract = True