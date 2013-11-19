# Server Specific Configurations
server = {
    'port': '9119',
    'host': '0.0.0.0'
}

# Pecan Application Configurations
app = {
    'root': 'kds.api.controllers.root.RootController',
    'modules': ['kds.api'],
    'static_root': '%(confdir)s/public',
    'template_path': '%(confdir)s/templates',
    'debug': False,
}

# Custom Configurations must be in Python dictionary format::
#
# foo = {'bar':'baz'}
#
# All configurations are accessible at::
# pecan.conf
