# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.
#
# hpctmanagers/__init__.py


"""Support for Manager class which encapsulates manager-type
functionality.
"""


import logging


logger = logging.getLogger(__name__)


class Manager:
    """Base Manager class.

    Overarching design goals:
    1. Manage one or more underlying services/servers/resources.
    2. High-level operations either succeed or fail.
    3. Control over low-level, individual items is not intended.

    This is not a library or debugging tool. The use case is defined
    and limited. Functionality is exposed and is intended to work or
    not. Anything that does not work is left up to the user/admin to
    address so that the Manager can work.

    The methods are a mix of functionality that one would find during
    the lifetime of a service/server/resource: install to start. The
    manager is not equivalent to an installer, systemd, etc. but
    does call on such functions to perform its work.
    """

    def __init__(self, *args, **kwargs):
        pass

    def configure(self):
        pass

    def disable(self):
        pass

    def enable(self):
        pass

    def install(self):
        pass

    def is_enabled(self):
        return False

    def is_installed(self):
        return False

    def is_running(self):
        return False

    def start(self):
        pass

    def stop(self):
        pass

    def restart(self):
        pass

    def uninstall(self):
        pass
