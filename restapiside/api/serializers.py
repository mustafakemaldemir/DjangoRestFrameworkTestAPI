from rest_framework import serializers
from restapiside.models import Article

class ArticleSerializer(serializers.Serializer):#create serializer so manuel mod step 1
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    comment = serializers.CharField()
    text = serializers.CharField()
    city = serializers.CharField()
    activity_status = serializers.BooleanField()
    published_date = serializers.DateField()
    created_date = serializers.DateTimeField(read_only=True)
    updated_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('yazar',instance.author)
        instance.title = validated_data.get('title',instance.title)
        instance.comment = validated_data.get('comment',instance.comment)
        instance.text = validated_data.get('text',instance.text)
        instance.city = validated_data.get('city',instance.city)
        instance.activity_status = validated_data.get('activity_status',instance.activity_status)
        instance.published_date = validated_data.get('published_date',instance.published_date)
        instance.save()
        return instance