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

import base64

from oslo.config import cfg
import pecan
from pecan import rest
import wsme
import wsmeext.pecan as wsme_pecan

# from kds.api.controllers.v1 import types
from kds.openstack.common.db.sqlalchemy import session as db_session
from kds.openstack.common.crypto import utils as cryptoutils
from kds.openstack.common import jsonutils
from kds.openstack.common import timeutils

CONF = cfg.CONF

get_engine = db_session.get_engine
get_session = db_session.get_session


class KeyRequest(wsme.types.Base):

    metadata = wsme.wsattr(wsme.types.text, mandatory=True)
    signature = wsme.wsattr(wsme.types.text, mandatory=True)

    def __init__(self, **kwargs):
        self._meta = None
        super(KeyRequest, self).__init__(**kwargs)

    @property
    def meta(self):
        if self._meta is None and self.metadata:
            self._meta = jsonutils.loads(base64.decodestring(self.metadata))

        return self._meta

    @meta.setter
    def meta(self, value):
        if value:
            self.metadata = base64.encodestring(jsonutils.dumps(value))
        else:
            self.metadata = None

        self._meta = value

    def verify_signature(self, crypto, key):
        try:
            sigc = crypto.sign(key, self.metadata)
        except Exception:
            raise exception.Unauthorized('Invalid Request')

        if sigc != self.signature:
            raise exception.Unauthorized('Invalid Request')

    def verify_expiration(self):
        now = timeutils.utcnow()

        try:
            timestamp = timeutils.parse_strtime(self.meta['timestamp'])
        except (AttributeError, ValueError):
            raise exception.Unauthorized('Invalid Timestamp')

        if (now - timestamp) > self.ttl:
            raise exception.Unauthorized('Invalid Request (expired)')


class KeyInput(wsme.types.Base):
    key = wsme.wsattr(wsme.types.binary, mandatory=True)


class KeyController(rest.RestController):

    @wsme_pecan.wsexpose(KeyRequest)
    def index(self):
        r = pecan.request
        meta = {'nonce': 'helloworld'}
        kr = KeyRequest(meta=meta, signature='sig')
        return kr

    @wsme.validate(wsme.types.text)
    @wsme_pecan.wsexpose(None, wsme.types.text, body=KeyInput, status=204)
    def put(self, key_name, key_input):
        pass

