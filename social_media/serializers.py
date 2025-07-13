from rest_framework import serializers

from social_media.models import Comment, Post
from social_media.validators import AgeValidator, TitleValidator


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор комментария"""

    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = ["id", "author", "text", "date_created", "date_updated"]


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор поста"""

    comments = CommentSerializer(source="post_comments", many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "text",
            "image",
            "author",
            "comments",
            "date_created",
            "date_updated",
        ]
        validators = [AgeValidator(field="author"), TitleValidator(field="title")]
