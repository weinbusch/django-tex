from django.db import models
from django.core.exceptions import ValidationError
from django.template import TemplateDoesNotExist
from django.utils.translation import ugettext_lazy as _
from django.template.loader import get_template


def validate_template_path(name):
    try:
        get_template(name, using='tex')
    except TemplateDoesNotExist:
        raise ValidationError(_('Template not found.'))


class TeXTemplateFile(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255, validators=[validate_template_path, ])

    class Meta:
        abstract = True
