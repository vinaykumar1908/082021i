from django.forms import ModelForm
from knowledge.models import KComment, KPost


class CommentForm(ModelForm):

    class Meta:
        model = KComment
        fields = ('text','commentfile')
