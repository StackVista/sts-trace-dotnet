call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\Tools\VsDevCmd.bat"


rem Restore NuGet packages
rem nuget.exe is required for command line restore because msbuild doesn't support packages.config
rem (see https://github.com/NuGet/Home/issues/7386)
nuget restore Datadog.Trace.sln

rem Build C# projects (Platform: always AnyCPU)
rem msbuild Datadog.Trace.proj /t:restore
msbuild Datadog.Trace.proj /t:restore /t:BuildCsharp /p:Configuration=Release

rem Build NuGet packages
dotnet pack src\Datadog.Trace\Datadog.Trace.csproj
dotnet pack src\Datadog.Trace.OpenTracing\Datadog.Trace.OpenTracing.csproj

rem The native profiler depends on the Datadog.Trace.ClrProfiler.Managed.Loader C# project so be sure that is built first
msbuild Datadog.Trace.proj /t:BuildCpp /p:Configuration=Release;Platform=x64
msbuild Datadog.Trace.proj /t:BuildCpp /p:Configuration=Release;Platform=x86

rem Build MSI installer for Windows x64 (supports both x64 and x86 apps)
msbuild Datadog.Trace.proj /t:msi /p:Configuration=Release;Platform=x64

rem Build MSI installer for Windows x86 (supports x86 apps only)
msbuild Datadog.Trace.proj /t:msi /p:Configuration=Release;Platform=x86

rem Build tracer home directory for Windows (x64 and x86)
msbuild Datadog.Trace.proj /t:CreateHomeDirectory /p:Configuration=Release;Platform=x64