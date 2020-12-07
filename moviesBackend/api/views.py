from .models import Movies
from rest_framework import viewsets
from .serializers import MoviesSerializer


class MoviesViewSet(viewsets.ModelViewSet):

    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
