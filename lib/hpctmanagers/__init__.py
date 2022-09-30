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

    Manages one or more underlying services/servers/resources.
    High-level operations that either succeed or fail. Control over
    low-level, individual items is not intended.

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
