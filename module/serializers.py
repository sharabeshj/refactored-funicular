from rest_framework import serializers
from module.models import Project,Module
from hashid_field.rest import HashidSerializerCharField

class ProjectSerializer(serializers.ModelSerializer):
	id = HashidSerializerCharField(source_field = 'module.Project.id')

	class Meta:
		model = Project
		fields = ('id','name')

class ModuleSerializer(serializers.ModelSerializer):
	id = HashidSerializerCharField(source_field = 'module.Module.id')
	project = serializers.PrimaryKeyRelatedField(pk_field = HashidSerializerCharField(source_field = 'module.Project.id'),queryset=Project.objects.all())

	class Meta:
		model = Module
		fields = ('id','name','project')