from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from module import views

router = DefaultRouter()
router.register(r'Project/getAllWithOutPagination',views.ProjectViewSet)
router.register(r'Module',views.ModuleViewSet)


urlpatterns = [
	url(r'^',include(router.urls))
]