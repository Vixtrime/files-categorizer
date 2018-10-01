from pyramid.view import view_config
from ..models import User
from pyramid.httpexceptions import HTTPFound
from pyramid.security import (
    remember,
    forget,
)


@view_config(route_name='signin', renderer='../templates/signin.jinja2')
def sign_in(request):
    # next_url = request.route_url('home')
    #
    # message = ''
    # login = ''
    #
    # if 'form.submit' in request.params:
    #     login = request.params['email']
    #     password = request.params['password']
    #     user = request.dbsession.query(User).filter(User.login == login).first()
    #     if user is not None and user.check_password(password):
    #         headers = remember(request, user.id)
    #         return HTTPFound(location=next_url, headers=headers)
    #     message = 'Failed login'

    return {}

# @view_config(route_name='signindata', renderer='ajax')
# def sign_in_data(request):
#
#     login = request.params['email']
#     password = request.params['password']
#
#     return {'user'}
