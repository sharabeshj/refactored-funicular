from rest_framework.routers import Route,DynamicRoute,DefaultRouter

class CustomRouter(DefaultRouter):
	routes = [
		Route(
				url = r'^{prefix}/getAllWithOutPagination$',
				mapping = {'get' : 'list'},
				name = '{basename}-list',
				detail = False,
				initkwargs = {'suffix' : 'List'}
			),
		Route(
				url = r'^{prefix}/getOne/{lookup}$',
				mapping = { 'get' : 'retrieve' },
				name = '{basename}-detail',
				detail = True,
				initkwargs = {'suffix' : 'Detail'}
			),
		Route(
				url = r'^{prefix}/create$',
				mapping = {'post' : 'create'},
				name = '{basename}-list',
				detail = False,
				initkwargs = {'suffix' : 'List'}
			),
		Route(
				url = r'^{prefix}/update$',
				mapping = {'post' : 'update'},
				name = '{basename}-detail',
				detail = True,
				initkwargs = {'suffix' : 'Detail'}
			),
		Route(
				url = r'^{prefix}/delete/{lookup}$',
				mapping = {'get' : 'destroy'},
				name = '{basename}-detail',
				detail = True,
				initkwargs = {'suffix' : 'Detail'}
			),
		DynamicRoute(
				url = r'^{prefix}/{url_path}/{lookup}$',
				name = '{basename}-{url_name}',
				detail = False,
				initkwargs = {}
			),
	]
