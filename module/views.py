from django.shortcuts import render
from rest_framework import viewsets
from module.models import Project,Module
from module.serializers import ProjectSerializer,ModuleSerializer
from rest_framework import permissions
from module.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer


class ModuleViewSet(viewsets.ModelViewSet):
	queryset = Module.objects.all()
	serializer_class = ModuleSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
							IsOwnerOrReadOnly,)
	
	@action(detail = False)
	def getAll(self,request,pk):
		try:
			get_module = Module.objects.filter(pk = pk)
			serializer = self.get_serializer_class()(get_module,many = True)
			return Response(serializer.data)		
		except :
			return Response(serializer.error)

