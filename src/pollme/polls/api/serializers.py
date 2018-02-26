
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)

from ..models import Question, Choice

class QuestionListSerializer(ModelSerializer):
    """
    This serializer serializes the Question model
    It should also include a field "choices" that will serialize all the
        choices for a question
    You well need a SerializerMethodField for choices,
        http://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
    Reference this stack overflow for the choices:
        https://stackoverflow.com/questions/33945148/return-nested-serializer-in-serializer-method-field
    """
    #choice = serializers.SerializerMethodField(source='get_question_choices')

    #def get_question_choices(self, obj):
     #   choices = obj.choice_set.all()
      #  return ChoiceSerializer(choices, many=True).data
    choices = SerializerMethodField(source='get_choices', read_only=True)

    def get_choices(self, obj):
        question_choices = obj.choice_set.all()
        return ChoiceSerializer(question_choices, many=True).data

    class Meta:
        model = Question
        fields = ('id', 'text', 'pub_date', 'choices')
    
class ChoiceSerializer(ModelSerializer):
    """
    This serializes the Choice model
    """
    class Meta:
        model = Choice
        fields = ('choice_text', 'votes')