# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.
#
# hpctmanagers/ubuntu.py

import apt
import subprocess

from . import ManagerException
from .systemd import SystemdManager


class UbuntuManager(SystemdManager):
    """Support Ubuntu system functionality.

    Set `install_packages` with list of packages to install."""

    install_packages = []

    def install(self):
        try:
            cache = apt.cache.Cache()
            cache.update()
            cache.open()

            for name in self.install_packages:
                cache[name].mark_install()

            cache.commit()
        except:
            ManagerException("failed to install packages")

    def is_installed(self):
        for name in self.install_packages:
            if subprocess.call(["dpkg", "-l", name]) != 0:
                return False
        return True
