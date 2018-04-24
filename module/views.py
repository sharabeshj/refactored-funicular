from django.shortcuts import render
from rest_framework import viewsets
from module.models import Project,Module
from module.serializers import ProjectSerializer,ModuleSerializer
from rest_framework import permissions
from module.permissions import IsOwnerOrReadOnly

# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer


class ModuleViewSet(viewsets.ModelViewSet):
	queryset = Module.objects.all()
	serializer_class = ModuleSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
							IsOwnerOrReadOnly,)


