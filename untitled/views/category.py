from pyramid.view import view_config
from ..models import File


@view_config(route_name='categoryFileAdd', renderer='json')
def category_processor(request):

    file_category_id = request.params['categoryId']
    category_name = request.params['categoryName']
    file_name = request.params['fileName']
    file_path = request.params['filePath']
    message = file_name + ' was successfully added to the ' + category_name
    success = True
    fp_exist = request.dbsession.query(File.file_path).filter(File.file_path == request.params['filePath']).first()

    if fp_exist:
        message = file_name + " is already exist in " + category_name
        success = False
    else:
        file = File(file_name=file_name, file_path=file_path, file_category_id=file_category_id)
        request.dbsession.add(file)

    return {'message': message, 'success': success}
