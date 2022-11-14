from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from books.models import Book, Author
from books.serializers import BooksSerializer


class BooksViewSet(viewsets.ModelViewSet):
    # queryset = Book.objects.all()
    serializer_class = BooksSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Book.objects.all()
        return Book.objects.filter(pk=pk)

    @action(methods=['get'], detail=False)
    def author(self, request):
        authors = Author.objects.all()
        return Response({'authors': [f'{author.firstname} {author.lastname}' for author in authors]})


# class BooksAPIView(views.APIView):
#     def get(self, request):
#         lst = Book.objects.all()
#         return Response({'books': BooksSerializer(lst, many=True).data})
#
#     def post(self, request):
#         serializer = BooksSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({'error': 'Method PUT not allowed'})
#
#         try:
#             instance = Book.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exist'})
#
#         serializer = BooksSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({'error': 'Method DELETE not allowed'})
#
#         try:
#             instance = Book.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exist'})
#
#         title = instance.title
#         instance.delete()
#         return Response({'post': f'Deleted book {title}'})


# devided by method
# class BooksAPIListPagination(PageNumberPagination):
#     page_size = 3
#     page_size_query_param = 'page_size'
#     max_page_size = 10000
#
#
# class BooksAPIView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BooksSerializer
#     permission_classes = (IsAuthenticated, )
#     authentication_classes = (TokenAuthentication, ) # does not work with JWT
#     pagination_class = BooksAPIListPagination
#
#
# class BooksAPIUpdate(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BooksSerializer
#
#
# class BooksAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BooksSerializer
