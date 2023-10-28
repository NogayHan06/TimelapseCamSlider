import octoprint.plugin

class TimelapseCamSlider(octoprint.plugin.StartupPlugin):
    def on_after_startup(self):
        self._logger.info("TimelapseCamSlider Ready || TimelapseCamSlider Hazır.")

    def get_update_information(*args, **kwargs):
        return dict(
            updateplugindemo=dict(
                displayName=self._plugin_name,
                displayVersion=self._plugin_version,

                type="github_release",
                current=self._plugin_version,
                user="NogayHan06",
                repo="TimelapseCamSlider",                
                pip="https://github.com/NogayHan06/TimelapseCamSlider/releases/download/ver.{target}/master.zip"
            )
        )

__plugin_pythoncompat__ = ">=3.7,<4"
__plugin_implementation__ = TimelapseCamSlider()
__plugin_hooks__ = {
"octoprint.plugin.softwareupdate.check_config": get_update_information
}
