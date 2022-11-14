import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from books.models import Book


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author')

    # if inherits serializers.Serializer:
    #
    # def create(self, validated_data):
    #     return Book.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.author_id = validated_data.get('author_id', instance.author_id)
    #     instance.save()
    #
    #     return instance

# under the hood:
# def encode():
#     model = BookModel('Beyond the wand')
#     model_sr = BooksSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title": "Beyond the wand"}')
#     data = JSONParser().parse(stream)
#     serializer = BooksSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
