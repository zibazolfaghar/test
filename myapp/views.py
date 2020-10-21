from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from .models import book
from .serializers import bookmodelserializer, bookserializer
from rest_framework.decorators import api_view, permission_classes


class getalldata(APIView):
    def get(self, request):
        query = book.objects.all().order_by('-create_at')
        serializers = bookmodelserializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def allApi(request):
    if request.method == 'GET':
        query = book.objects.all().order_by('-create_at')
        serializers = bookmodelserializer(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class getfavdata(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        query = book.objects.filter(fav=True)
        serializers = bookmodelserializer(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class updatefavdata(APIView):
    pass
    # def get(self, request, pk):
    #     query = book.objects.get(pk=pk)
    #     serializers = bookmodelserializer(query)
    #     return Response(serializers.data, status=status.HTTP_200_OK)

    # def put(self, request, pk):
    #     query = book.objects.get(pk=pk)
    #     serializers = bookmodelserializer(query, data=request.data)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response(serializers.data, status=status.HTTP_201_CREATED)
    #     return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def setdata(request):
    serializers = bookmodelserializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class postmodeldata(APIView):
    def post(self, request):
        serializers = bookmodelserializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class postdata(APIView):
    def post(self, request):
        serializers = bookserializer(data=request.data)
        if serializers.is_valid():
            author = serializers.data.get('Author')
            store_name = serializers.data.get('store_name')
            description = serializers.data.get('description')
            image = request.FILES['image']
            fav = serializers.data.get('fav')
        else:
            return Response(serializers.errors, status=status.HTTP_404_NOT_FOUND)
        Book = book()
        Book.Author = author
        Book.store_name = store_name
        Book.description = description
        Book.image = image
        Book.fav = fav
        Book.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)


class searchdata(APIView):
    def get(self, request):
        search = request.GET['name']
        query = book.objects.filter(store_name__contains=search)
        serializers = bookmodelserializer(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class deletedata(APIView):
    def get(self, request, pk):
        query = book.objects.get(pk=pk)
        serializers = bookmodelserializer(query)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        query = book.objects.get(pk=pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        query = book.objects.get(pk=pk)
        serializers = bookmodelserializer(query, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def calc(request):
    try:
        num1 = request.data["num1"]
        num2 = request.data["num2"]
        operator = request.data["operator"]
    except:
        return Response({"error": "send num1 and num2 and operator"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        if isinstance(num1, int) and isinstance(num2, int):
            if operator == "add":
                return Response({"result": num1 + num2}, status=status.HTTP_200_OK)
            elif operator == "sub":
                return Response({"result": num1 - num2}, status=status.HTTP_200_OK)
            elif operator == "div":
                return Response({"result": num1 / num2}, status=status.HTTP_200_OK)
            elif operator == "mul":
                return Response({"result": num1 * num2}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "send integers values"}, status=status.HTTP_400_BAD_REQUEST)
            pass
        else:
            return Response({"error": "send integer values"}, status=status.HTTP_400_BAD_REQUEST)
