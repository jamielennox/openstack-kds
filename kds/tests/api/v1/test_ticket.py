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

from kds.tests.api.v1 import base
from kds.openstack.common import jsonutils
from kds.openstack.common import timeutils

REQUEST_KEY = base64.b64decode('LDIVKc+m4uFdrzMoxIhQOQ==')
TARGET_KEY = base64.b64decode('EEGfTxGFcZiT7oPO+brs+A==')

TEST_KEY = base64.b64decode('Jx5CVBcxuA86050355mTrg==')

DEFAULT_REQUESTOR = 'home.local'
DEFAULT_TARGET = 'tests.openstack.remote'
DEFAULT_GROUP = 'home'
DEFAULT_NONCE = '42'

EMPTY_CONTEXT = {}


class TicketTests(base.BaseTestCase):

    def _ticket_metadata(self, requestor=DEFAULT_REQUESTOR,
                         target=DEFAULT_TARGET, nonce=DEFAULT_NONCE,
                         timestamp=None, b64encode=True):
        if not timestamp:
            timestamp = timeutils.utcnow()

        metadata = {'requestor': requestor, 'target': target,
                    'nonce': nonce, 'timestamp': timestamp}

        if b64encode:
            metadata = base64.b64encode(jsonutils.dumps(metadata))

        return metadata

    def test_ticket(self):
        r = self.get("/key")
        return r
