schema = {
    'rootPath': {
        'type': 'string',
        'required': True,
    },
    'path': {
        'type': 'string',
        'required': True,
        'unique': True
    },
    'isdir': {
        'type': 'boolean',
        'default': False,
    },
    'info': {
        'type': 'dict',
        'default': {},
    }

}
ufile = {
    'item_itile': 'ufile',
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST', 'DELETE'],
    'item_methods': ['GET', 'PATCH', 'PUT', 'DELETE'],

    'schema': schema
}
