"""
Agent namespaced tasks
"""
from __future__ import print_function
import glob
import os
import shutil
import sys
import platform
from distutils.dir_util import copy_tree

import invoke
from invoke import task
from invoke.exceptions import Exit

from .utils import do_sed_rename, do_sed_rename_quoted

# constants

@task
def apply_branding(ctx):
    """
    Apply stackstate branding
    """
    sts_camel_replace = 's/Data[dD]og/StackState/g'
    sts_lower_replace = 's/datadog/stackstate/g'
    datadog_metrics_replace = 's/"datadog./"stackstate./g'

    # Installer mocking

    do_sed_rename_quoted(ctx, "s/datadoghq\.com\/support/stackstate\.io/g",
                  "./deploy/Datadog.Trace.ClrProfiler.WindowsInstaller/Product.wxs")

    do_sed_rename_quoted(ctx, "s/datadoghq\.com/stackstate\.io/g",
                  "./deploy/Datadog.Trace.ClrProfiler.WindowsInstaller/Product.wxs")
    do_sed_rename_quoted(ctx, "s/\\\"Datadog, Inc./\\\"Stackstate/g",
                  "./deploy\Datadog.Trace.ClrProfiler.WindowsInstaller\Config.wxi")
    do_sed_rename_quoted(ctx, "s/\\\"Datadog/\\\"Stackstate/g",
                  "./deploy\Datadog.Trace.ClrProfiler.WindowsInstaller\Config.wxi")
    