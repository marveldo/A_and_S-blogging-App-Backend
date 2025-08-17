from rest_framework import serializers
from .models import Blog


class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        extra_kwargs = {
            'author': {
                'read_only': True
            },
            'title': {
                'required': False
            },
            'content': {
                'required': False

            },
            'status': {
                'required': False

            }
        }

    def validate(self, attrs: dict):
        if self.instance == None:
            if not attrs.get('content'):
                raise serializers.ValidationError({'content': 'Content field is required'})
            if not attrs.get('title'):
                raise serializers.ValidationError({'title': 'Title field is required'})
        
        return super().validate(attrs)

    def create(self, validated_data: dict):
        user = self.context.get('request').user
        blog = Blog.objects.create(author=user, **validated_data)
        blog.save()
        return blog
            


