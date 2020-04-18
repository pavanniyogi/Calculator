from .views import calculate

def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('calc', '/action/{operator}/{firstOper}/{secondOper}')
    config.add_view(calculate.main_calculator, route_name='calc')