# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.
#
# hpctmanagers/systemd.py

import subprocess

from . import Manager, ManagerException


class SystemdManager(Manager):
    """Support systemd-specific functionality.

    Set `systemd_services` with list of systemd items to manage."""

    systemd_services = []

    def disable(self):
        """Disable services."""

        try:
            rc = 0
            for name in self.systemd_services:
                if (
                    subprocess.call(
                        ["systemctl", "disable", name],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.STDOUT,
                    )
                    != 0
                ):
                    rc = 1
        finally:
            if rc != 0:
                raise ManagerException("failed to disable services")

    def enable(self):
        """Enable services."""

        try:
            rc = 0
            for name in self.systemd_services:
                if (
                    subprocess.call(
                        ["systemctl", "enable", name],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.STDOUT,
                    )
                    != 0
                ):
                    rc = 1
        finally:
            if rc != 0:
                raise ManagerException("failed to enable services")

    def is_enabled(self):
        """Check enabled status of services."""

        for name in self.systemd_services:
            if (
                subprocess.call(
                    ["systemctl", "is-enabled", name],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT,
                )
                != 0
            ):
                return False
        return True

    def is_running(self):
        """Check running/active status of services."""

        for name in self.systemd_services:
            if (
                subprocess.call(
                    ["systemctl", "is-active", name],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT,
                )
                != 0
            ):
                return False
        return True

    def start(self):
        """Start services."""

        try:
            rc = 0
            for name in self.systemd_services:
                if (
                    subprocess.call(
                        ["systemctl", "start", name],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.STDOUT,
                    )
                    != 0
                ):
                    rc = 1
        finally:
            if rc != 0:
                raise ManagerException("failed to start services")

    def stop(self):
        """Stop services."""

        try:
            rc = 0
            for name in self.systemd_services:
                if (
                    subprocess.call(
                        ["systemctl", "stop", name],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.STDOUT,
                    )
                    != 0
                ):
                    rc = 1
        finally:
            if rc != 0:
                raise ManagerException("failed to stop services")
