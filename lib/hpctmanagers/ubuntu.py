# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.
#
# hpctmanagers/ubuntu.py

import apt

from . import ManagerException
from .systemd import SystemdManager


class UbuntuManager(SystemdManager):
    """Support Ubuntu system functionality.

    Set `install_packages` with list of packages to install.

    Set `install_snaps` with dictionary for packages to install.
    The supported dictionary fields are:
    * name: snap package name
    * channel: channel to pull from
    * version: snap package version
    """

    install_packages = []
    install_snaps = []

    def __init__(self, *args, **kwargs):
        if "install_packages" in kwargs:
            self.install_packages = kwargs.pop("install_packages")
        if "install_snaps" in kwargs:
            self.install_snaps = kwargs.pop("install_snaps")

        super().__init__(*args, **kwargs)

    def _install_debs(self):
        try:
            failed = []

            cache = apt.cache.Cache()
            cache.update()
            cache.open()

            for name in self.install_packages:
                if not self._is_installed_deb(name):
                    try:
                        cache[name].mark_install()
                        cache.commit()
                    except:
                        failed.append(name)
        except:
            failed = "-"
        finally:
            if failed:
                raise ManagerException(
                    f"({self.__class__.__name__}) failed to install packages ({failed})"
                )

    def _install_snaps(self):
        try:
            failed = []

            for snapd in self.install_snaps:
                if self._is_installed_snap(snapd):
                    continue

                # needs install/refresh
                args = ["snap", "install", snapd["name"]]
                if channel := snapd.get("channel"):
                    args.append(f"--channel={channel}")
                args.extend(snapd.get("args", []))

                if self._verbose:
                    cp = self._run(args, decorate=True)
                else:
                    cp = self._run_quiet(args)
                if cp.returncode != 0:
                    failed.append(snapd["name"])
        except:
            failed = "-"
        finally:
            if failed:
                raise ManagerException(
                    f"({self.__class__.__name__}) failed to install snaps ({failed})"
                )

    def _is_installed_deb(self, name):
        return True if self._call_quiet(["dpkg", "-l", name]) == 0 else False

    def _is_installed_snap(self, snapd):
        # TODO: check for version
        return True if self._call_quiet(["snap", "list", snapd["name"]]) == 0 else False

    def install(self):
        self._install_debs()
        self._install_snaps()

    def is_installed(self):
        for name in self.install_packages:
            if not self._is_installed_deb(name):
                return False

        for snapd in self.install_snaps:
            if not self._is_installed_snap(snapd):
                return False

        return True
