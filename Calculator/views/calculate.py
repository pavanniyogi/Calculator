from pyramid.view import view_config

@view_config(route_name='calc', renderer='json')
def main_calculator(request):
    try:
        if request.matchdict['operator'] == 'sum':
            output = int(request.matchdict['firstOper']) + int(request.matchdict['secondOper'])
            return {'result' : output}
        else:
            return {'result' : 'Future changes are yet to be implemented'}
    except Exception as e:
        return {'Error': e}




