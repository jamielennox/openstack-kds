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

from kds.tests.api.v1 import base


class KeyCrudTests(base.BaseTestCase):

    # def test_key_bad_set(self):
    #     self.put('/key/test.key')
    #     self.put('/key/test.key', body={'hello': 'world'})
    #     self.put('/key/test.key', body={'key': "{'hello': 'world'}"})

    def test_store_key(self):
        self.put('/key/test.key', json={'key': 'dbad4234'}, expected_status=204)

    # def test_overwrite_key(self):
    #     self.contrib_kds_api.store_key('home.local', TEST_KEY)
    #     self.assertEqual(self.contrib_kds_api.retrieve_key('home.local'),
    #                      TEST_KEY)
    #     self.contrib_kds_api.store_key('home.local', REQUEST_KEY)
    #     self.assertEqual(self.contrib_kds_api.retrieve_key('home.local'),
    #                      REQUEST_KEY)
