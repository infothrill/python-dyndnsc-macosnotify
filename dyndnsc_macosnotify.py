# -*- coding: utf-8 -*-

"""Package for dyndnsc_macosnotify."""

__version__ = "0.1"

import os

from pync import Notifier


class MacOsNotify(object):
    """Send desktop notifications with OS X notification center."""

    def after_remote_ip_update(self, ip, status):
        """
        Handle the after_remote_ip_update plugin hook.

        :param ip: ip address
        :param status: string
        """
        default_title = "Dynamic DNS"
        if status == 0:
            message = "Remote IP updated to %s" % ip
        else:
            message = "Problem updating remote IP to %s" % ip
        Notifier.notify(message, title=default_title, group=os.getpid())
