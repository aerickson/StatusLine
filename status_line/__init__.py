# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class StatusLinePlugin(octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.AssetPlugin,
                       octoprint.plugin.OctoPrintPlugin
                       ):

    def __init__(self):
        pass

    def hook_m117(self, comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
        if gcode and gcode == "M117":
            self._logger.debug("Sent M117 command: {0}".format(cmd))
            self._plugin_manager.send_plugin_message(self._identifier, dict(status_line=cmd[5:]))

    def get_assets(self):
        return {
            "js": ["js/status_line.js"]
        }

    def get_template_configs(self):
        return [
            dict(type="sidebar", name="Status line", icon="print")
        ]

__plugin_name__ = "Status Line"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = StatusLinePlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.comm.protocol.gcode.sent": __plugin_implementation__.hook_m117
    }
