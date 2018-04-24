from django.conf.urls import url,include
from module import views
from module.routers import CustomRouter

router = CustomRouter()
router.register(r'Project',views.ProjectViewSet)
router.register(r'Module',views.ModuleViewSet)


urlpatterns = [
	url(r'^',include(router.urls))
]