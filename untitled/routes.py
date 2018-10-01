def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('signin', '/signin')
    config.add_route('categoryFileAdd', '/category/file/add')
    config.add_route('viewcatalog', '/{catalogname}')
    config.add_route('signindata', '/signindata')
