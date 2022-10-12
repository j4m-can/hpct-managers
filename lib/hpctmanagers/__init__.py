# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.
#
# hpctmanagers/__init__.py


"""Support for Manager class which encapsulates manager-type
functionality.
"""

import grp
import os
import pathlib
import pwd
import subprocess


class ManagerException(Exception):
    pass


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

    def _call(self, *args, **kwargs):
        """Unmodified subprocess.call() helper."""

        return subprocess.call(*args, **kwargs)

    def _call_quiet(self, cmd, *args, **kwargs):
        """Helper for quiet subprocess.call()."""

        return subprocess.call(
            cmd, *args, **kwargs, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT
        )

    def _call_capture(self, cmd, *args, **kwargs):
        """Helper for capture subprocess.call()."""

        return subprocess.call(cmd, *args, **kwargs, capture_output=True)

    def _run(self, *args, **kwargs):
        """Unmodified subprocess.run() helper."""

        return subprocess.run(*args, **kwargs)

    def _run_quiet(self, cmd, *args, **kwargs):
        """Helper for quiet subprocess.run()."""

        return subprocess.run(
            cmd, *args, **kwargs, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT
        )

    def _run_capture(self, cmd, *args, **kwargs):
        """Helper for catpure subprocess.run()."""

        return subprocess.run(cmd, *args, **kwargs, capture_output=True)

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

    def restart(self):
        self.stop()
        self.start()

    def save_file(self, data, path, mode=None, user=None, group=None):
        """Save file."""

        try:
            user = user if user != None else -1
            group = group if group != None else -1
            uid = user if type(user) == int else pwd.getpwnam(user).pw_uid
            gid = group if type(group) == int else grp.getgrnam(group).gr_gid
        except:
            raise Exception("could not find owner/group")

        try:
            # create/update securely
            p = pathlib.Path(path)
            p.touch()

            if (uid, gid) != (-1, -1):
                os.chown(path, uid, gid)

            if mode != None:
                p.chmod(mode)

            p.write_bytes(self.data)
        except:
            raise Exception("failed to save file")

    def save_file_by_key(self, data, key, mode=None, user=None, group=None):
        """Look up file settings by key and call `save_file()`."""
        pass

    def start(self):
        pass

    def stop(self):
        pass
