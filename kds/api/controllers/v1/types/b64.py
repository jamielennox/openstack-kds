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

import wsme

from kds.openstack.common import jsonutils


class Base64Type(wsme.types.UserType):
    """
    A user type that use base64 strings to carry string data.

    This is the same object as the wsme BinaryType however with the basetype
    of text rather than bytes.
    """
    basetype = wsme.types.text
    name = 'base64'

    def tobasetype(self, value):
        if value is None:
            return None
        return base64.encodestring(value)

    def frombasetype(self, value):
        if value is None:
            return None
        return base64.decodestring(value)


class Base64JsonType(Base64Type):

    basetype = None
    name = 'base64json'

    def tobasetype(self, value):
        text = jsonutils.dumps(value)
        return super(Base64JsonType, self).tobasetype(text)

    def frombasetype(self, value):
        text = super(Base64JsonType, self).frombasetype(value)
        return jsonutils.loads(text)

