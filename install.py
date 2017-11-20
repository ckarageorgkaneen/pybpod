#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pip, os
from subprocess import call

SUBMODULES_FOLDERS = [
    'logging-bootstrap',
    'pysettings',
    'pyforms',
    'pyforms-generic-editor',
    'pybpod-api',
    'pybpod-gui-api',
    'pybranch',
    'pybpod-gui-plugin',
    'pybpod-gui-plugin-session-history',
    'pybpod-gui-plugin-timeline',
    'pybpod-rotary-encoder-module',
]

DEFAULT_PLUGINS = [
    'pybpodgui_plugin',
    'pybpodgui_plugin_timeline',
    'pybpodgui_plugin_session_history',
    'pybpod-rotary-encoder-module'
]




def install():
    for submodule in SUBMODULES_FOLDERS:
        pip.main(['install', '--upgrade', os.path.join(submodule,'.')])

def check_submodules():
    for submodule in SUBMODULES_FOLDERS:
        if not os.path.exists(os.path.join(submodule,'setup.py')):
            call(["git", "pull", "--recurse-submodules"])
            break

def conf_default_settings():
    if not os.path.exists('user_settings.py'):
        f = open('user_settings.py', 'w')
        f.write("SETTINGS_PRIORITY = 0\n\n")
        f.write("GENERIC_EDITOR_PLUGINS_LIST = "+str(DEFAULT_PLUGINS))
        f.close()


if __name__=='__main__': 
    install()
    conf_default_settings()