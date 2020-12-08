
from rest_framework import viewsets
from .serializers import MoviesSerializer
from .models import Movies


def list(request, *args, **kwargs):
    movies = Movies.objects.all()
    serializer = MoviesMiniSerializer(movies, many=True)
    return Response(serializer.data)


class MoviesViewSet(viewsets.ModelViewSet):

    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
