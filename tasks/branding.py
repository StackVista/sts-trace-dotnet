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

from .utils import do_sed_rename, do_sed_rename_quoted, do_file_replace, do_dll_replace

# constants

@task
def apply_branding(ctx):
    """
    Apply stackstate branding
    """
    sts_camel_replace = 's/Data[dD]og/StackState/g'
    sts_lower_replace = 's/datadog/stackstate/g'
    datadog_metrics_replace = 's/"datadog./"stackstate./g'

# Directory.Build.props
    do_file_replace(
        ctx,
        "Directory.Build.props",
        "<!-- StyleCop -->",
        """

  <PropertyGroup>
    <AssemblyName>$(MSBuildProjectName.Replace("Datadog.", "StackVista."))</AssemblyName>
    <PackageId>$(MSBuildProjectName.Replace("Datadog.", "StackVista."))</PackageId>
  </PropertyGroup>

  <!-- StyleCop -->
        """
        )

# src/Datadog.Trace.ClrProfiler.Managed.Core/AssemblyInfo.cs
    do_file_replace(
        ctx,
        "src/Datadog.Trace.ClrProfiler.Managed.Core/AssemblyInfo.cs",
        "InternalsVisibleTo(\"Datadog.Trace",
        "InternalsVisibleTo(\"StackVista.Trace"
        )

# src/Datadog.Trace.ClrProfiler.Managed.Core/AssemblyInfo.cs
    do_file_replace(
        ctx,
        "src/Datadog.Trace.ClrProfiler.Managed.Core/AssemblyInfo.cs",
        "InternalsVisibleTo(\"Datadog.Trace",
        "InternalsVisibleTo(\"StackVista.Trace"
        )

# src/Datadog.Trace.ClrProfiler.Managed/AssemblyInfo.cs
    do_file_replace(
        ctx,
        "src/Datadog.Trace.ClrProfiler.Managed/AssemblyInfo.cs",
        "InternalsVisibleTo(\"Datadog.Trace",
        "InternalsVisibleTo(\"StackVista.Trace"
        )

# src/Datadog.Trace.OpenTracing/AssemblyInfo.cs
    do_file_replace(
        ctx,
        "src/Datadog.Trace.OpenTracing/AssemblyInfo.cs",
        "InternalsVisibleTo(\"Datadog.Trace",
        "InternalsVisibleTo(\"StackVista.Trace"
        )

# src/Datadog.Trace/AssemblyInfo.cs
    do_file_replace(
        ctx,
        "src/Datadog.Trace/AssemblyInfo.cs",
        "InternalsVisibleTo(\"Datadog.Trace",
        "InternalsVisibleTo(\"StackVista.Trace"
        )

# src/Directory.Build.props
    do_file_replace(
        ctx,
        "src/Directory.Build.props",
        "</project>",
        """
       <!-- sts-property-group -->
       <PropertyGroup>
          <AssemblyName>$(MSBuildProjectName.Replace("Datadog.", "StackVista."))</AssemblyName>
          <PackageId>$(MSBuildProjectName.Replace("Datadog.", "StackVista."))</PackageId>
       </PropertyGroup>
       </project>
        """
        )


# test/Datadog.Trace.Tests/Logging/LoggingProviderTestHelpers.cs
    do_file_replace(
        ctx,
        "test/Datadog.Trace.Tests/Logging/LoggingProviderTestHelpers.cs",
        "[Datadog.Trace.Tests.Logging]",
        "[StackVista.Trace.Tests.Logging]"
        )

# test/Directory.Build.props
    do_file_replace(
        ctx,
        "test/Directory.Build.props",
        "<!-- StyleCop -->",
        """

  <PropertyGroup>
    <AssemblyName>$(MSBuildProjectName.Replace("Datadog.", "StackVista."))</AssemblyName>
    <PackageId>$(MSBuildProjectName.Replace("Datadog.", "StackVista."))</PackageId>
  </PropertyGroup>

  <!-- StyleCop -->
        """
        )

# Datadog.Trace.proj
    do_file_replace(
        ctx,
        "Datadog.Trace.proj",
        "Datadog.Trace.ClrProfiler.Native.dll",
        "StackVista.Trace.ClrProfiler.Native.dll"
        )

# Directory.Build.props
    do_file_replace(
        ctx,
        "Directory.Build.props",
        "</Project>",
        """

  <!-- StackVista Overrides -->
  <PropertyGroup>
    <AssemblyName>$(MSBuildProjectName.Replace("Datadog.", "StackVista."))</AssemblyName>
    <TargetName>$(TargetName.Replace("Datadog.", "StackVista."))</TargetName>
    <AssemblyOriginatorKeyFile>$(AssemblyOriginatorKeyFile.Replace("Datadog.", "StackVista."))</AssemblyOriginatorKeyFile>
  </PropertyGroup>
</Project>
        """
        )

# deploy/Datadog.Trace.ClrProfiler.WindowsInstaller/Files.Managed.Net45.GAC.wxs
    do_dll_replace(ctx, "deploy/Datadog.Trace.ClrProfiler.WindowsInstaller/Files.Managed.Net45.GAC.wxs")

# deploy/Datadog.Trace.ClrProfiler.WindowsInstaller/Files.Managed.Net45.wxs
    do_dll_replace(ctx, "deploy/Datadog.Trace.ClrProfiler.WindowsInstaller/Files.Managed.Net45.wxs")

# deploy/Datadog.Trace.ClrProfiler.WindowsInstaller/Files.Managed.Net461.wxs
    do_dll_replace(ctx, "deploy/Datadog.Trace.ClrProfiler.WindowsInstaller/Files.Managed.Net461.wxs")

# deploy/Datadog.Trace.ClrProfiler.WindowsInstaller/Files.Managed.NetStandard20.wxs
    do_dll_replace(ctx, "deploy/Datadog.Trace.ClrProfiler.WindowsInstaller/Files.Managed.NetStandard20.wxs")

# deploy/Datadog.Trace.ClrProfiler.WindowsInstaller/Product.wxs
    do_dll_replace(ctx, "deploy/Datadog.Trace.ClrProfiler.WindowsInstaller/Product.wxs")

# docker/Datadog.Trace.ClrProfiler.IntegrationTests.sh
    do_dll_replace(ctx, "docker/Datadog.Trace.ClrProfiler.IntegrationTests.sh")

# integrations.json

    do_file_replace(
        ctx,
        "integrations.json",
        "Datadog.Trace.AspNet",
        "StackVista.Trace.AspNet"
        )
    do_file_replace(
        ctx,
        "integrations.json",
        "Datadog.Trace.ClrProfiler.Managed.Core",
        "StackVista.Trace.ClrProfiler.Managed.Core"
        )        
    do_file_replace(
        ctx,
        "integrations.json",
        "Datadog.Trace.ClrProfiler.Managed",
        "StackVista.Trace.ClrProfiler.Managed"
        )        
    do_file_replace(
        ctx,
        "integrations.json",
        "Datadog.Trace",
        "StackVista.Trace"
        )        
    do_file_replace(
        ctx,
        "integrations.json",
        "def86d061d0d2eeb",
        "6b12922542db680e"
        )        

# performance/Performance.StackExchange.Redis/Properties/launchSettings.json
    do_dll_replace(ctx, "performance/Performance.StackExchange.Redis/Properties/launchSettings.json")

# reproduction-dependencies/AppDomain.Instance/Properties/launchSettings.json
    do_dll_replace(ctx, "reproduction-dependencies/AppDomain.Instance/Properties/launchSettings.json")

# reproductions/AssemblyLoad.FileNotFoundException/Properties/launchSettings.json
    do_dll_replace(ctx, "reproductions/AssemblyLoad.FileNotFoundException/Properties/launchSettings.json")

# reproductions/AssemblyResolveMscorlibResources.InfiniteRecursionCrash/Properties/launchSettings.json
    do_dll_replace(ctx, "reproductions/AssemblyResolveMscorlibResources.InfiniteRecursionCrash/Properties/launchSettings.json")

# reproductions/AutomapperTest/Properties/launchSettings.json
    do_dll_replace(ctx, "reproductions/AutomapperTest/Properties/launchSettings.json")

# reproductions/HttpMessageHandler.StackOverflowException/Properties/launchSettings.json
    do_dll_replace(ctx, "reproductions/HttpMessageHandler.StackOverflowException/Properties/launchSettings.json")

# reproductions/OrleansCrash/Properties/launchSettings.json
    do_dll_replace(ctx, "reproductions/OrleansCrash/Properties/launchSettings.json")

# reproductions/SecurityGrant.FileNotFoundException/Properties/launchSettings.json
    do_dll_replace(ctx, "reproductions/SecurityGrant.FileNotFoundException/Properties/launchSettings.json")

# reproductions/StackExchange.Redis.AssemblyConflict.LegacyProject/Program.cs
    do_dll_replace(ctx, "reproductions/StackExchange.Redis.AssemblyConflict.LegacyProject/Program.cs")

# reproductions/StackExchange.Redis.AssemblyConflict.SdkProject/Program.cs
    do_dll_replace(ctx, "reproductions/StackExchange.Redis.AssemblyConflict.SdkProject/Program.cs")

# reproductions/StackExchange.Redis.AssemblyConflict.SdkProject/Properties/launchSettings.json
    do_dll_replace(ctx, "reproductions/StackExchange.Redis.AssemblyConflict.SdkProject/Properties/launchSettings.json")

# reproductions/StackExchange.Redis.StackOverflowException/Properties/launchSettings.json
    do_dll_replace(ctx, "reproductions/StackExchange.Redis.StackOverflowException/Properties/launchSettings.json")

# samples-aspnet/Samples.AspNetMvc4/Views/Home/Index.cshtml
    do_dll_replace(ctx, "samples-aspnet/Samples.AspNetMvc4/Views/Home/Index.cshtml")

# samples-aspnet/Samples.AspNetMvc5/Views/Home/Index.cshtml
    do_dll_replace(ctx, "samples-aspnet/Samples.AspNetMvc5/Views/Home/Index.cshtml")

# samples-aspnet/Samples.AspNetMvc5_0/Views/Home/Index.cshtml
    do_dll_replace(ctx, "samples-aspnet/Samples.AspNetMvc5_0/Views/Home/Index.cshtml")

# samples-aspnet/Samples.WebForms.Empty/App_Code/Profiler.cs
    do_dll_replace(ctx, "samples-aspnet/Samples.WebForms.Empty/App_Code/Profiler.cs")

# samples/Samples.AspNetCoreMvc21/Properties/launchSettings.json
    do_dll_replace(ctx, "samples/Samples.AspNetCoreMvc21/Properties/launchSettings.json")

# samples/Samples.AspNetCoreMvc21/Views/Home/Index.cshtml
    do_dll_replace(ctx, "samples/Samples.AspNetCoreMvc21/Views/Home/Index.cshtml")

# samples/Samples.AspNetCoreMvc30/Properties/launchSettings.json
    do_dll_replace(ctx, "samples/Samples.AspNetCoreMvc30/Properties/launchSettings.json")

# samples/Samples.AspNetCoreMvc31/Properties/launchSettings.json
    do_dll_replace(ctx, "samples/Samples.AspNetCoreMvc30/Properties/launchSettings.json")

# samples/Samples.Dapper/Properties/launchSettings.json
    do_dll_replace(ctx, "samples/Samples.Dapper/Properties/launchSettings.json")

# samples/Samples.Elasticsearch.MultipleAppDomains/Properties/launchSettings.json
    do_dll_replace(ctx, "samples/Samples.Elasticsearch.MultipleAppDomains/Properties/launchSettings.json")

# samples/Samples.Elasticsearch.V5/Properties/launchSettings.json
    do_dll_replace(ctx, "samples/Samples.Elasticsearch.V5/Properties/launchSettings.json")

# samples/Samples.Elasticsearch/Properties/launchSettings.json
    do_dll_replace(ctx, "samples/Samples.Elasticsearch/Properties/launchSettings.json")

# samples/Samples.FakeAzureAppServices/Properties/launchSettings.json
    do_dll_replace(ctx, "samples/Samples.FakeAzureAppServices/Properties/launchSettings.json")

# samples/Samples.FakeKudu/Properties/launchSettings.json
    do_dll_replace(ctx, "samples/Samples.FakeKudu/Properties/launchSettings.json")

# samples/Samples.GraphQL/Properties/launchSettings.json
    do_dll_replace(ctx, "samples/Samples.GraphQL/Properties/launchSettings.json")

# samples/Samples.HttpMessageHandler/Properties/launchSettings.json
    do_dll_replace(ctx, "samples/Samples.HttpMessageHandler/Properties/launchSettings.json")

# samples/Samples.MongoDB/Properties/launchSettings.json
    do_dll_replace(ctx, "samples/Samples.MongoDB/Properties/launchSettings.json")

# samples/Samples.MySql/Properties/launchSettings.json
    do_dll_replace(ctx, "samples/Samples.MySql/Properties/launchSettings.json")

# samples/Samples.Npgsql/Properties/launchSettings.json
    do_dll_replace(ctx, "samples/Samples.Npgsql/Properties/launchSettings.json")

# samples/Samples.RateLimiter/Properties/launchSettings.json
    do_dll_replace(ctx, "samples/Samples.RateLimiter/Properties/launchSettings.json")

# samples/Samples.ServiceStack.Redis/Properties/launchSettings.json
    do_dll_replace(ctx, "samples/Samples.ServiceStack.Redis/Properties/launchSettings.json")

# samples/Samples.SqlServer/Properties/launchSettings.json
    do_dll_replace(ctx, "samples/Samples.SqlServer/Properties/launchSettings.json")

# samples/Samples.StackExchange.Redis/Properties/launchSettings.json
    do_dll_replace(ctx, "samples/Samples.StackExchange.Redis/Properties/launchSettings.json")

# samples/Samples.TracingWithoutLimits/Properties/launchSettings.json
    do_dll_replace(ctx, "samples/Samples.TracingWithoutLimits/Properties/launchSettings.json")

# samples/Samples.Wcf/Properties/launchSettings.json
    do_dll_replace(ctx, "samples/Samples.Wcf/Properties/launchSettings.json")

# src/Datadog.Trace.ClrProfiler.Managed.Core/AssemblyInfo.cs
    do_file_replace(
        ctx,
        "src/Datadog.Trace.ClrProfiler.Managed.Core/AssemblyInfo.cs",
        "002400000480000094000000060200000024000052534131000400000100010025b855c8bc41b1d47e777fc247392999ca6f553cdb030fac8e3bd010171ded9982540d988553935f44f7dd58cb4b17fbb92653d5c2dc5112696886665b317c6f92795bf64beab2405c501c8a30cb1b31b1541ed66e27d9823169ec2815b00ceeeecc8d5a1bf43db67d2961a3e9bea1397f043ec07491709649252f5565b756c5",
        "002400000480000094000000060200000024000052534131000400000100010071fda5b460f39c72b5ef25e6c4b4cb0e606e452187639d9c5f7b9775b577735e3b8af39c305b9df3fff0a76105f824b31f8565f7a7c96d2373254fbc611faafb665588d0b82ddf4b557919c15d68fb9fd34a7224c5137648fbae319f269b23b1d7aaac7f02625200af1c1c182aedc2cc98318e16d083b6b4030ce1ee94aaa7aa"
        )

# src/Datadog.Trace.ClrProfiler.Managed/AssemblyInfo.cs
    do_file_replace(
        ctx,
        "src/Datadog.Trace.ClrProfiler.Managed/AssemblyInfo.cs",
        "002400000480000094000000060200000024000052534131000400000100010025b855c8bc41b1d47e777fc247392999ca6f553cdb030fac8e3bd010171ded9982540d988553935f44f7dd58cb4b17fbb92653d5c2dc5112696886665b317c6f92795bf64beab2405c501c8a30cb1b31b1541ed66e27d9823169ec2815b00ceeeecc8d5a1bf43db67d2961a3e9bea1397f043ec07491709649252f5565b756c5",
        "002400000480000094000000060200000024000052534131000400000100010071fda5b460f39c72b5ef25e6c4b4cb0e606e452187639d9c5f7b9775b577735e3b8af39c305b9df3fff0a76105f824b31f8565f7a7c96d2373254fbc611faafb665588d0b82ddf4b557919c15d68fb9fd34a7224c5137648fbae319f269b23b1d7aaac7f02625200af1c1c182aedc2cc98318e16d083b6b4030ce1ee94aaa7aa"
        )

# src/Datadog.Trace.ClrProfiler.Managed/NativeMethods.cs
    do_dll_replace(ctx, "src/Datadog.Trace.ClrProfiler.Managed/NativeMethods.cs")

# src/Datadog.Trace.ClrProfiler.Native/Datadog.Trace.ClrProfiler.Native.DLL.vcxproj
    do_file_replace(
        ctx,
        "src/Datadog.Trace.ClrProfiler.Native/Datadog.Trace.ClrProfiler.Native.DLL.vcxproj",
        "Datadog.Trace.AspNet",
        "StackVista.Trace.AspNet"
        )
    do_file_replace(
        ctx,
        "src/Datadog.Trace.ClrProfiler.Native/Datadog.Trace.ClrProfiler.Native.DLL.vcxproj",
        "Datadog.Trace.ClrProfiler.Managed.Core",
        "StackVista.Trace.ClrProfiler.Managed.Core"
        )        
    do_file_replace(
        ctx,
        "src/Datadog.Trace.ClrProfiler.Native/Datadog.Trace.ClrProfiler.Native.DLL.vcxproj",
        "Datadog.Trace.ClrProfiler.Managed",
        "StackVista.Trace.ClrProfiler.Managed"
        )        
    do_file_replace(
        ctx,
        "src/Datadog.Trace.ClrProfiler.Native/Datadog.Trace.ClrProfiler.Native.DLL.vcxproj",
        "Datadog.Trace",
        "StackVista.Trace"
        )        

# src/Datadog.Trace.ClrProfiler.Native/Datadog.Trace.ClrProfiler.Native.def
    do_dll_replace(ctx, "src/Datadog.Trace.ClrProfiler.Native/Datadog.Trace.ClrProfiler.Native.def")

# src/Datadog.Trace.ClrProfiler.Native/Resource.rc
    do_file_replace(
        ctx,
        "src/Datadog.Trace.ClrProfiler.Native/Resource.rc",
        "Datadog.Trace",
        "StackVista.Trace"
        )

# src/Datadog.Trace.ClrProfiler.Native/cor_profiler.cpp
    do_file_replace(
        ctx,
        "src/Datadog.Trace.ClrProfiler.Native/cor_profiler.cpp",
        "DATADOG",
        "STACKVISTA"
        )

# src/Datadog.Trace.OpenTracing/AssemblyInfo.cs
    do_file_replace(
        ctx,
        "src/Datadog.Trace.OpenTracing/AssemblyInfo.cs",
        "002400000480000094000000060200000024000052534131000400000100010025b855c8bc41b1d47e777fc247392999ca6f553cdb030fac8e3bd010171ded9982540d988553935f44f7dd58cb4b17fbb92653d5c2dc5112696886665b317c6f92795bf64beab2405c501c8a30cb1b31b1541ed66e27d9823169ec2815b00ceeeecc8d5a1bf43db67d2961a3e9bea1397f043ec07491709649252f5565b756c5",
        "002400000480000094000000060200000024000052534131000400000100010071fda5b460f39c72b5ef25e6c4b4cb0e606e452187639d9c5f7b9775b577735e3b8af39c305b9df3fff0a76105f824b31f8565f7a7c96d2373254fbc611faafb665588d0b82ddf4b557919c15d68fb9fd34a7224c5137648fbae319f269b23b1d7aaac7f02625200af1c1c182aedc2cc98318e16d083b6b4030ce1ee94aaa7aa"
        )


# src/Datadog.Trace/AssemblyInfo.cs
    do_file_replace(
        ctx,
        "src/Datadog.Trace/AssemblyInfo.cs",
        "002400000480000094000000060200000024000052534131000400000100010025b855c8bc41b1d47e777fc247392999ca6f553cdb030fac8e3bd010171ded9982540d988553935f44f7dd58cb4b17fbb92653d5c2dc5112696886665b317c6f92795bf64beab2405c501c8a30cb1b31b1541ed66e27d9823169ec2815b00ceeeecc8d5a1bf43db67d2961a3e9bea1397f043ec07491709649252f5565b756c5",
        "002400000480000094000000060200000024000052534131000400000100010071fda5b460f39c72b5ef25e6c4b4cb0e606e452187639d9c5f7b9775b577735e3b8af39c305b9df3fff0a76105f824b31f8565f7a7c96d2373254fbc611faafb665588d0b82ddf4b557919c15d68fb9fd34a7224c5137648fbae319f269b23b1d7aaac7f02625200af1c1c182aedc2cc98318e16d083b6b4030ce1ee94aaa7aa"
        )

# src/Directory.Build.props
    do_file_replace(
        ctx,
        "src/Directory.Build.props",
        "</Project>",
        """

  <!-- StackVista Overrides -->
  <PropertyGroup>
    <PackageId>$(MSBuildProjectName.Replace("Datadog.", "StackVista."))</PackageId>
    <!-- Override any of the above Package items -->
  </PropertyGroup>
</Project>
        """
        )

# test/Datadog.Trace.ClrProfiler.IntegrationTests/HttpClientTests.cs
    do_file_replace(
        ctx,
        "test/Datadog.Trace.ClrProfiler.IntegrationTests/HttpClientTests.cs",
        "Datadog.Trace",
        "StackVista.Trace"
        )


# test/Datadog.Trace.TestHelpers/EnvironmentHelper.cs
    do_file_replace(
        ctx,
        "test/Datadog.Trace.TestHelpers/EnvironmentHelper.cs",
        "Datadog.Trace",
        "StackVista.Trace"
        )

# tools/PrepareRelease/SetAllVersions.cs
    do_file_replace(
        ctx,
        "tools/PrepareRelease/SetAllVersions.cs",
        "Datadog.Trace",
        "StackVista.Trace"
        )

    do_file_replace(
        ctx,
        "tools/PrepareRelease/SetAllVersions.cs",
        "def86d061d0d2eeb",
        "6b12922542db680e"
        )


    # # Installer mocking

    # do_sed_rename_quoted(ctx, "s/datadoghq\.com\/support/stackstate\.io/g",
    #               "./deploy/Datadog.Trace.ClrProfiler.WindowsInstaller/Product.wxs")

    # do_sed_rename_quoted(ctx, "s/datadoghq\.com/stackstate\.io/g",
    #               "./deploy/Datadog.Trace.ClrProfiler.WindowsInstaller/Product.wxs")
    # do_sed_rename_quoted(ctx, "s/\\\"Datadog, Inc./\\\"Stackstate/g",
    #               "./deploy\Datadog.Trace.ClrProfiler.WindowsInstaller\Config.wxi")
    # do_sed_rename_quoted(ctx, "s/\\\"Datadog/\\\"Stackstate/g",
    #               "./deploy\Datadog.Trace.ClrProfiler.WindowsInstaller\Config.wxi")
    