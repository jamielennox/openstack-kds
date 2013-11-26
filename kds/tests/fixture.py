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

import fixtures

from kds.common import config
from kds.openstack.common.db.sqlalchemy import session as db_session
from kds.openstack.common import timeutils


class Conf(fixtures.Fixture):
    """Fixture to manage global conf settings."""

    _SQL_CONNECTION = 'sqlite:///kds.db'

    def __init__(self, conf):
        self.conf = conf

    def setUp(self):
        super(Conf, self).setUp()

        db_session.set_defaults(sql_connection=self._SQL_CONNECTION,
                                sqlite_db='kds.sqlite')

        self.conf.set_default('master_key_file', 'test.mkey', group='kds')
        self.conf.set_default('connection', "sqlite://", group='database')
        self.conf.set_default('verbose', True)

        config.parse_args(args=[])
        self.addCleanup(self.conf.reset)


class TimeOverride(fixtures.Fixture):
    """Fixture to start and remove time override."""

    def setUp(self):
        super(TimeOverride, self).setUp()
        timeutils.set_time_override()
        self.addCleanup(timeutils.clear_time_override)
