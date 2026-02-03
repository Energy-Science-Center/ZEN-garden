from zen_garden.core.plugin_manager import PluginManager


def test_plugin_manager():
    """
    Tests if plugin manager can discover known example plugins.
    """
    pm = PluginManager()
    discovered = set(pm.discover_plugins())
    pm.print_plugins()

    # All known plugins should be discovered
    expected = {
        "zen_garden.plugins.test_plugin",
    }
    assert discovered == expected
