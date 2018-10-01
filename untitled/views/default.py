from pyramid.view import view_config
import os
from ..models.category import Category


@view_config(route_name='home', renderer='../templates/layout.jinja2')
def my_view(request):

    root_dir_path = request.registry.settings['root_dir_path']

    def file_list(path):
        tree = []
        for item in os.listdir(path):
            item_path = path + '\\' + item
            item_info = {}
            if os.path.isdir(item_path):
                item_info['type'] = 'directory'
                item_info['path'] = item_path
                item_info['name'] = os.path.basename(item_path)
                item_info['childs'] = file_list(item_path)
            else:
                item_info['type'] = 'file'
                item_info['name'] = os.path.basename(item_path)
                item_info['path'] = item_path
            tree.append(item_info)
        return tree

    filesystem = file_list(root_dir_path)
    category = request.dbsession.query(Category).all()

    return {'filesystem': filesystem, 'category': category}
