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

import os

from oslo.config import cfg

from kds.openstack.common import test
from kds.tests import fixture

TEST_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
ROOT_DIR = os.path.normpath(os.path.join(TEST_DIR, '..', '..'))

CONF = cfg.CONF


class BaseTestCase(test.BaseTestCase):

    def setUp(self):
        super(BaseTestCase, self).setUp()
        self.useFixture(fixture.Conf(CONF))

    # can't use the word tests here
    def tst_path(self, *args):
        return os.path.join(TEST_DIR, *args)

    def root_path(self, *args):
        return os.path.join(ROOT_DIR, *args)
