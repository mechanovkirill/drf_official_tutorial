
from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly, IsOwnerOrStuff
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import permissions, renderers, viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # FIXME: seems it works incorrect with user-list ReadOnlyModelViewSet
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrStuff]


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)