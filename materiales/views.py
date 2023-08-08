from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, authentication, permissions, generics, serializers
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response

from django.db.models import Count, Sum, Q

from django_filters.rest_framework import DjangoFilterBackend

from . import serializers
from rest_framework.permissions import IsAuthenticated
from materiales.serializers import (
    ArticuloSerializer,
    EjemplarSerializer,
    TipoMaterialSerializer,
    AutorSerializer,
    CarreraSerializer,
    GeneroSerializer,
    EditorialSerializer,

    ReservasSerializer,
    PrestamosSerializer,
)

from accounts.models import User
from materiales.models import (
    Articulo,
    Ejemplar,
    TipoMaterial,
    Autor,
    Carrera,
    Genero,
    Editorial,
    Reservas,
    Prestamos

)

"""
# Primero definimos los elementos del modelo Articulo
"""


class CarreraViewSet(viewsets.ModelViewSet):
    serializer_class = CarreraSerializer
    queryset = Carrera.objects.all()


class GeneroViewSet(viewsets.ModelViewSet):
    serializer_class = GeneroSerializer
    queryset = Genero.objects.all()


class EditorialViewSet(viewsets.ModelViewSet):
    serializer_class = EditorialSerializer
    queryset = Editorial.objects.all()


class TipoMaterialViewSet(viewsets.ModelViewSet):
    serializer_class = TipoMaterialSerializer
    queryset = TipoMaterial.objects.all()


class AutorViewSet(viewsets.ModelViewSet):
    serializer_class = AutorSerializer
    queryset = Autor.objects.all()


class TituloView(generics.ListAPIView):
    serializer_class = serializers.ArticuloNameSerializer
    queryset = Articulo.objects.all()


class ReservasView(generics.ListAPIView):
    serializer_class = serializers.ListReservaSerializer
    queryset = Reservas.objects.all()


class ReservaCreateView(generics.ListCreateAPIView):
    permission_classess = (IsAuthenticated,)

    serializer_class = serializers.CreateReservaserializer
    queryset = Reservas.objects.all()

    def get(self, request):
        user = request.user
        response = {
            'status': status.HTTP_200_OK,
            'owner': user
        }
        return Response(response, content_type='application/json')


class ReservaDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ListReservaSerializer
    queryset = Reservas.objects.all()

    def retrieve(self, request, *args, **kwargs):
        super(ReservaDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Successfully retrieved",
            "result": data,
        }
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(ReservaDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Successfully updated",
            "result": data,
        }
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(ReservaDetailView, self).delete(request, args, kwargs)
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Successfully deleted",
        }
        return Response(response)


class CreatePrestamoView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PrestamosSerializer
    queryset = Prestamos.objects.all()


class CreateArticuloView(generics.ListCreateAPIView):

    serializer_class = ArticuloSerializer
    queryset = Articulo.objects.all()


class DetailArticuloView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articulo.objects.all()
    serializer_class = serializers.ListArticuloSerializer

    def retrieve(self, request, *args, **kwargs):
        super(DetailArticuloView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Successfully retrieved",
            "result": data,
        }
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(DetailArticuloView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Successfully updated",
            "result": data,
        }
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(DetailArticuloView, self).delete(request, args, kwargs)
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Successfully deleted",
        }
        return Response(response)


class ListEjemplarView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = serializers.ListEjemplarSerializer
    queryset = Ejemplar.objects.all()


class CreateEjemplarView(generics.ListCreateAPIView):
    serializer_class = serializers.EjemplarSerializer
    queryset = Ejemplar.objects.all()


class DetailEjemplarView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.EjemplarSerializer
    queryset = Ejemplar.objects.all()

    def retrieve(self, request, *args, **kwargs):
        super(DetailEjemplarView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Successfully retrieved",
            "Ejemplar": data,
        }
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(DetailEjemplarView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Successfully updated",
            "Ejemplar": data,
        }
        return Response(response)


"""    user = request.user
    articulo = self.get_object()
    serializer = ArticuloSerializer(data=request.data)
    if user.role == 5:
"""


class ListArticuloView(generics.ListAPIView):
    serializer_class = serializers.ListArticuloSerializer
    permission_classes = (AllowAny,)
    queryset = Articulo.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['titulo', 'tipo', 'autor', 'genero', ]


"""     stock = Ejemplar.objects.values('articulo').annotate(
        cant_ejemplares=Count('articulo'),
        cant_disponibles=Count('estado', filter=Q(estado='d'))
    )
    for item in stock:      
            if item['cant_disponibles'] > 0:       
                print(item)
                print(item['articulo'], item['cant_disponibles'])
 """
