from pyramid.view import view_config
from ..models import Category, File
from pyramid.httpexceptions import (
    HTTPNotFound,
    )


@view_config(route_name='viewcatalog', renderer='../templates/viewcatalog.jinja2')
def view_catalog(request):
    pagename = request.matchdict['catalogname']
    page = request.dbsession.query(Category).filter_by(category_name=pagename).first()
    if page is None:
        raise HTTPNotFound('No such page')

    category_content = request.dbsession.query(File)\
        .filter(File.file_category_id == page.category_id)\
        .all()

    return {'pagename': pagename, 'page': page, 'category_content': category_content}
