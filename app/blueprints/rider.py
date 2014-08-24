from flask import Blueprint, request, Response, json
from mongoengine import connect
from mongoengine.queryset import NotUniqueError
from app.api.services.rider_service import RiderService

rider_bp = Blueprint('rider_bp', __name__, template_folder='templates')

@rider_bp.record
def rider_setup(state):
    rider_bp.service = RiderService()

@rider_bp.route('/rider/', methods=['GET', 'POST', 'PUT'])
@rider_bp.route('/rider/<rid>', methods=['GET', 'PUT', 'DELETE'])
def riderAPI(rid=None):
    """REST API for riders.
    XXX Note: rid is current the rider number, not the mongodb id.
    :param rid - rider number
    """
    if request.method == 'GET':
        if rid:
            rider = rider_bp.service.find(rid)
            if rider:
                return Response(
                    rider.to_json(),
                    status=200,
                    mimetype='application/json'
                )
            else:
                return Response(status=404)
        else:
            all_riders = rider_bp.service.find()
            if len(all_riders):
                return Response(
                    all_riders.to_json(),
                    status=200,
                    mimetype='application/json'
                )
            else:
                return Response(status=404)

    if request.method == 'POST':
        try:
            saved = rider_bp.service.create(json.loads(request.data))
            rider = rider_bp.service.find(saved.id)
            return Response(
                rider.to_json(),
                status=201,
                mimetype='application/json'
            )
        except NotUniqueError as e:
            print e
            resp = {
                'error': True,
                'msg': 'Rider number is already taken'
            }
            return Response(json.dumps(resp), status=400)
        except Exception as e:
            print e
            resp = {
                'error': True,
                'msg': 'Uncaught Error creating rider.'
            }
            return Response(json.dumps(resp), status=500)

    if request.method == 'PUT':
        try:
            if rid:
                saved = rider_bp.service.update(rid, json.loads(request.data))
                rider = rider_bp.service.find(saved.id)
                return Response(
                    rider.to_json(),
                    status=200,
                    mimetype='application/json'
                )
            else:
                saved = rider_bp.service.create(json.loads(request.data))
                rider = rider_bp.service.find(saved.id)
                return Response(
                    rider.to_json(),
                    status=201,
                    mimetype='application/json'
                )
        except NotUniqueError as e:
            print e
            resp = {
                'error': True,
                'msg': 'Rider number is already taken'
            }
            return Response(json.dumps(resp), status=400)
        except Exception as e:
            print e
            resp = {
                'error': True,
                'msg': 'Uncaught Error creating rider.'
            }
            return Response(json.dumps(resp), status=500)

    if request.method == 'DELETE':
        if rid:
            ret = rider_bp.service.delete(rid)
            if ret['error']:
                return Response(
                    ret['msg'],
                    status=500,
                    mimetype='application/json'
                )
            else:
                return Response(
                    ret['msg'],
                    status=200,
                    mimetype='application/json'
                )
