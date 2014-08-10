from flask import Blueprint, request, Response, json
from mongoengine import connect
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
            rider = rider_bp.service.find_riders(rid)
            if rider:
                return Response(
                    rider.to_json(),
                    status=200,
                    mimetype='application/json'
                )
            else:
                return Response(status=404)
        else:
            all_riders = rider_bp.service.find_riders()
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
            rider = rider_bp.service.create_rider(json.loads(request.data))
            return Response(
                json.dumps(rider.to_dict()),
                status=201,
                mimetype='application/json'
            )
        except Exception as e:
            msg = 'Error creating rider %s' % e
            print msg
            return Response(msg, status=500)

    if request.method == 'PUT':
        if rid:
            rider = rider_bp.service.update_rider(rid, json.loads(request.data))
            return Response(
                json.dumps(rider.to_dict()),
                status=200,
                mimetype='application/json'
            )
        else:
            try:
                rider = rider_bp.service.create_rider(json.loads(request.data))
                return Response(
                    json.dumps(rider.to_dict()),
                    status=201,
                    mimetype='application/json'
                )
            except Exception as e:
                msg = 'Error creating rider %s' % e
                print msg
                return Response(msg, status=500)

    if request.method == 'DELETE':
        if rid:
            ret = rider_bp.service.delete_rider(rid)
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
