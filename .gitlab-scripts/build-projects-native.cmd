call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\Tools\VsDevCmd.bat"

rem Restore NuGet packages
rem nuget.exe is required for command line restore because msbuild doesn't support packages.config
rem (see https://github.com/NuGet/Home/issues/7386)
nuget restore Datadog.Trace.sln

dotnet build src/Datadog.Trace.ClrProfiler.Managed.Loader/Datadog.Trace.ClrProfiler.Managed.Loader.csproj
dotnet build sample-libs/Samples.ExampleLibrary/Samples.ExampleLibrary.csproj
dotnet build sample-libs/Samples.ExampleLibraryTracer/Samples.ExampleLibraryTracer.csproj

rem Build C# projects (Platform: always AnyCPU)
msbuild Datadog.Trace.proj /t:BuildCsharp /p:Configuration=Debug

rem Build NuGet packages
rem --no-build, we did that already and we need to make sure the correct ones are packaged.
dotnet pack src\Datadog.Trace\Datadog.Trace.csproj --no-build
dotnet pack src\Datadog.Trace.OpenTracing\Datadog.Trace.OpenTracing.csproj --no-build

rem Build C++ projects

rem The native profiler depends on the Datadog.Trace.ClrProfiler.Managed.Loader C# project so be sure that is built first
msbuild Datadog.Trace.proj /t:BuildCpp;BuildCppTests /p:Configuration=Release;Platform=x64
msbuild Datadog.Trace.proj /t:BuildCpp;BuildCppTests /p:Configuration=Release;Platform=x86

rem Build MSI installer for Windows x64 (supports both x64 and x86 apps)
msbuild Datadog.Trace.proj /t:msi /p:Configuration=Debug;Platform=x64

rem Build MSI installer for Windows x86 (supports x86 apps only)
msbuild Datadog.Trace.proj /t:msi /p:Configuration=Debug;Platform=x86

rem Build tracer home directory for Windows (x64 and x86)
msbuild Datadog.Trace.proj /t:CreateHomeDirectory /p:Configuration=Debug;Platform=x64