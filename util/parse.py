def parse_mongo_resp(response):
    """Since mongo's queryset has a to_json method, but no dict method.  This
    is a problem because flask-restful automatically json encodes what you
    return, therefore double encoding the response, making it invalid json.

    This takes a mongo response, converts it to a dict and returns that.
    :param - response mongoengine QuerySet result
    """
    import json
    return json.loads(response.to_json())
