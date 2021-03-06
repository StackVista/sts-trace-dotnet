call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\Tools\VsDevCmd.bat"


rem Restore NuGet packages
rem nuget.exe is required for command line restore because msbuild doesn't support packages.config
rem (see https://github.com/NuGet/Home/issues/7386)
echo "================== Restore NuGet packages"
nuget restore Datadog.Trace.sln

rem Build C# projects (Platform: always AnyCPU)
rem msbuild Datadog.Trace.proj /t:restore
echo "================== Build C# projects (Platform: always AnyCPU)"
msbuild Datadog.Trace.proj /t:restore /t:BuildCsharp /p:Configuration=Release

rem Build NuGet packages
echo "==================> Build NuGet packages"
dotnet pack src\Datadog.Trace\Datadog.Trace.csproj --configuration Release
dotnet pack src\Datadog.Trace.OpenTracing\Datadog.Trace.OpenTracing.csproj --configuration Release

rem The native profiler depends on the Datadog.Trace.ClrProfiler.Managed.Loader C# project so be sure that is built first
echo "================== Datadog.Trace.ClrProfiler.Managed.Loader C# project"
msbuild Datadog.Trace.proj /t:BuildCpp /p:Configuration=Release;Platform=x64
msbuild Datadog.Trace.proj /t:BuildCpp /p:Configuration=Release;Platform=x86

rem Build MSI installer for Windows x64 (supports both x64 and x86 apps)
echo "================== MSI x64"
msbuild Datadog.Trace.proj /t:msi /p:Configuration=Release;Platform=x64

rem Build MSI installer for Windows x86 (supports x86 apps only)
echo "================== MSI x86"
msbuild Datadog.Trace.proj /t:msi /p:Configuration=Release;Platform=x86

rem Build tracer home directory for Windows (x64 and x86)
echo "================== tracer home directory (x64 and x86)"
msbuild Datadog.Trace.proj /t:CreateHomeDirectory /p:Configuration=Release;Platform=x64