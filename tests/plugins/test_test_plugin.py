from zen_garden.core.plugin_manager import PluginManager, Hook

def test_test_plugin():

    plugin_config = {
        "test_plugin": {
          "config": {
            "config1": "value1"
          }
        }
      }

    pm = PluginManager()
    pm.register(plugin_config)
    pm.emit(Hook.BEFORE_OPTIMIZATION_CONSTRUCTION, optimization_setup={})
    pm.emit(Hook.AFTER_OPTIMIZATION_CONSTRUCTION, optimization_setup={}, model_instance={})

