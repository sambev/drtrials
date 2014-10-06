def wants_json(mimetypes):
    """See if the client wants json by inspecting the mimetypes
    :param {werkzeug.datastructures.MIMEAccept}
    :return {bool} True|False - True if we should return json
    """
    best = mimetypes.best_match(['application/json', 'text/html'])
    return best == 'application/json'

