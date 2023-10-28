import octoprint.plugin

class TimelapseCamSlider(octoprint.plugin.StartupPlugin):
    def on_after_startup(self):
        self._logger.info("TimelapseCamSlider Ready || TimelapseCamSlider Hazır.")

__plugin_pythoncompat__ = ">=3.7,<4"
__plugin_implementation__ = TimelapseCamSlider()