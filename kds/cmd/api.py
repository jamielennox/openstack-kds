# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import logging
import sys

from oslo.config import cfg
from wsgiref import simple_server

from kds.api import app
from kds.common import service
from kds.openstack.common import log

PROJECT = 'kds'
CONF = cfg.CONF


def main():
    service.prepare_service(sys.argv)

    # Build and start the WSGI app
    host = CONF.bind_ip
    port = CONF.port
    wsgi = simple_server.make_server(host, port,
                                     app.VersionSelectorApplication())

    LOG = log.getLogger(__name__)
    LOG.info("Serving on http://%s:%s" % (host, port))
    LOG.info("Configuration:")
    CONF.log_opt_values(LOG, logging.INFO)

    try:
        wsgi.serve_forever()
    except KeyboardInterrupt:
        pass
