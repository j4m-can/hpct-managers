# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.
#
# hpctmanagers/systemd.py

from . import Manager, ManagerException


class SystemdManager(Manager):
    """Support systemd-specific functionality.

    Set `systemd_services` with list of systemd items to manage."""

    systemd_services = []

    def __init__(self, *args, **kwargs):
        if "systemd_services" in kwargs:
            self.systemd_services = kwargs.pop("systemd_services")

        super().__init__(*args, **kwargs)

    def disable(self):
        """Disable services."""

        try:
            rc = 0
            for name in self.systemd_services:
                if self._call_quiet(["systemctl", "disable", name]) != 0:
                    rc = 1
        finally:
            if rc != 0:
                raise ManagerException(f"({self.__class__.__name__}) failed to disable services")

    def enable(self):
        """Enable services."""

        try:
            rc = 0
            for name in self.systemd_services:
                if self._call_quiet(["systemctl", "enable", name]) != 0:
                    rc = 1
        finally:
            if rc != 0:
                raise ManagerException(f"({self.__class__.__name__}) failed to enable services")

    def is_enabled(self):
        """Check enabled status of services."""

        for name in self.systemd_services:
            if self._call_quiet(["systemctl", "is-enabled", name]) != 0:
                return False
        return True

    def is_running(self):
        """Check running/active status of services."""

        for name in self.systemd_services:
            if self._call_quiet(["systemctl", "is-active", name]) != 0:
                return False
        return True

    def start(self):
        """Start services."""

        try:
            rc = 0
            for name in self.systemd_services:
                if self._call_quiet(["systemctl", "start", name]) != 0:
                    rc = 1
        finally:
            if rc != 0:
                raise ManagerException(f"({self.__class__.__name__}) failed to start services")

    def stop(self):
        """Stop services."""

        try:
            rc = 0
            for name in self.systemd_services:
                if self._call_quiet(["systemctl", "stop", name]) != 0:
                    rc = 1
        finally:
            if rc != 0:
                raise ManagerException(f"({self.__class__.__name__}) failed to stop services")
