from rest_framework import status
from rest_framework.views import Response
from rest_framework.decorators import api_view
from .models import Person
from .serializers import PersonSerializer
import json

# Create your views here.
@api_view(['GET', 'POST',])
def person_list(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        serializerData = PersonSerializer(persons, many = True)
        return Response(serializerData.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
          name = request.data.get('name')
          if type(name) != str:
              response_data = {"response":"Can accept only string"}
              return Response(response_data)
          Person.objects.create(name=name)
          response_data = {"response":"person Created"}
          return Response(response_data, status = status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def person_detail(request):
    try:
        # Check the content type of the request, decode and extract it
        content_type = request.headers.get('content-type', '')

        if 'application/json' in content_type:
            data = json.loads(request.body.decode('utf-8'))
            id = data.get('id')
            name = data.get('name')
            person = Person.objects.filter(id=id).first()
            #person = Person.objects.get(id=id)

    except Person.DoesNotExist:
        response_data = {"response":"Person does not exists"}
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializerData = PersonSerializer(person)
        if person is None:
            response_data = {"response":"Person does not exists"}
            return Response(response_data)
        return Response(serializerData.data)


    elif request.method == 'PUT':
         if name is None:
             response_data = {"response":"Name parameter needed"}
             return Response(response_data,status=status.HTTP_404_NOT_FOUND)
         person.name = name
         person.save()
         response_data = {"response":"Person Updated"}
         return Response(response_data,status=status.HTTP_200_OK)


    elif request.method == 'DELETE':
         if person is None:
             response_data = {"response":"Person does not exists"}
             return Response(response_data,status=status.HTTP_404_NOT_FOUND)
         person.delete()
         response_data = {"response":"person Deleted"}
         return Response(response_data,status=status.HTTP_200_OK)
        

  