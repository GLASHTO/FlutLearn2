from rest_framework import serializers

from .models import Discussion, Comments, User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'created_date'
        )

class DiscussionCreateSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default = serializers.CurrentUserDefault())

    class Meta:
        model = Discussion
        fields = (
            'user',
            'title',
            'description'
        )

class CommentsCreateSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default = serializers.CurrentUserDefault())

    class Meta:
        model = Comments
        fields = (
            'user',
            'text'
        )

class DiscussionListSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Discussion
        fields = (
            'id',
            'user',
            'title'
        )
class DiscussionDetailSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Discussion
        fields = '__all__'

class CommentsListSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Comments
        fields = (
            'id',
            'user',
            'text'
        )

class CommentDetailSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    discussion = DiscussionDetailSerializer()

    class Meta:
        model = Comments
        fields = '__all__'
