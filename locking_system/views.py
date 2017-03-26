from django.shortcuts import get_object_or_404

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import Resource


class RequestResourceApiView(GenericAPIView):

    def get_object(self):
        return get_object_or_404(Resource, pk=self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        resource = self.get_object()
        if resource.status == resource.LOCKED:
            return Response(
                {'status': 'This resource is already taken. please check in a couple of seconds.'},
                status=400
            )

        resource.status = resource.LOCKED
        resource.save()
        return Response({'status': 'success'}, status=200)


class ReleaseResourceApiView(GenericAPIView):

    def get_object(self):
        return get_object_or_404(Resource, pk=self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        resource = self.get_object()
        resource.status = resource.RELEASED
        resource.save()
        return Response({'status': 'success'}, status=200)
