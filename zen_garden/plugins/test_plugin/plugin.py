from zen_garden.plugins.base_plugin import BasePlugin
from zen_garden.core.plugin_manager import Hook
from zen_garden.core.utils import setup_logger

import logging

setup_logger()

class Plugin(BasePlugin):

    name = "Test Plugin"
    hooks = {
        Hook.BEFORE_OPTIMIZATION_CONSTRUCTION,
        Hook.AFTER_OPTIMIZATION_CONSTRUCTION,
    }
    config_template = {
      "config1": "TestString"
    }

    def before_optimization_construction(self, optimization_setup):
        """
        Test hook method.

        :return: A test string indicating the plugin is active.
        :rtype: str
        """
        logging.info(f"Plugin {self.name} can perform actions before optimization construction.")

    def after_optimization_construction(self, optimization_setup, model_instance):
        """
        Test hook method.

        :return: A test string indicating the plugin is active.
        :rtype: str
        """
        logging.info(f"Plugin {self.name} can perform actions after optimization construction.")
