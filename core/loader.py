import importlib
import os

def load_plugins(plugin_folder: str = "plugins"):
    plugins = []
    for file in os.listdir(plugin_folder):
        if file.endswith(".py") and not file.startswith("__"):
            module_name = f"{plugin_folder}.{file[:-3]}"
            module = importlib.import_module(module_name)
            plugins.append(module)
    return plugins
