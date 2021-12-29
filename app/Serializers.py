from drf_queryfields import QueryFieldsMixin
from rest_framework import serializers

from app.models import User, Project, News, ProjectNews


class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)


class UserSerializers(QueryFieldsMixin, serializers.ModelSerializer):
    type = ChoiceField(choices=User.UserType)
    last_login = serializers.DateTimeField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'type', 'last_login']


class ProjectSerializers(QueryFieldsMixin, serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Project
        fields = '__all__'


class NewsSerializers(QueryFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = News
        fields = '__all__'

class ProjectNewsSerializers(QueryFieldsMixin, serializers.ModelSerializer):
    project_ser = ProjectSerializers(read_only=True, source='project')
    news_ser = NewsSerializers(read_only=True, source='news')
    class Meta:
        model = ProjectNews
        fields = ['project', 'news', 'highlight', 'project_ser', 'news_ser']




