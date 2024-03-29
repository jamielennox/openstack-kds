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

from kds.tests.api import base


def v1_url(*args):
    return base.urljoin('v1', *args)


class BaseTestCase(base.BaseTestCase):

    def get(self, url, *args, **kwargs):
        return super(BaseTestCase, self).get(v1_url(url), *args, **kwargs)

    def post(self, url, *args, **kwargs):
        return super(BaseTestCase, self).post(v1_url(url), *args, **kwargs)

    def put(self, url, *args, **kwargs):
        return super(BaseTestCase, self).put(v1_url(url), *args, **kwargs)
