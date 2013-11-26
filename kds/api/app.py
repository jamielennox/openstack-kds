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

import pecan

from kds.api import config as pecan_config
from kds.api import hooks
from kds.common import config as oslo_config

CONF = oslo_config.CONF


def get_pecan_config():
    # Set up the pecan configuration
    filename = pecan_config.__file__.replace('.pyc', '.py')
    return pecan.configuration.conf_from_file(filename)


def setup_app(config=None, extra_hooks=None):
    app_hooks = [hooks.ConfigHook(),
                 hooks.StorageHook(),
                 hooks.CryptoManager()]

    if extra_hooks:
        app_hooks.extend(extra_hooks)

    if not config:
        config = get_pecan_config()

    pecan.configuration.set_config(dict(config), overwrite=True)

    app = pecan.make_app(
        config.app.root,
        static_root=config.app.static_root,
        template_path=config.app.template_path,
        debug=CONF.debug,
        force_canonical=getattr(config.app, 'force_canonical', True),
        hooks=app_hooks,
    )

    return app


class VersionSelectorApplication(object):
    def __init__(self):
        pc = get_pecan_config()
        self.v1 = setup_app(config=pc)

    def __call__(self, environ, start_response):
        return self.v1(environ, start_response)
