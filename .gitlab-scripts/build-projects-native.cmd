call "C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Auxiliary\Build\vcvarsall.bat" x86_amd64

dotnet build src/Datadog.Trace.ClrProfiler.Managed.Loader/Datadog.Trace.ClrProfiler.Managed.Loader.csproj
dotnet build sample-libs/Samples.ExampleLibrary/Samples.ExampleLibrary.csproj
dotnet build sample-libs/Samples.ExampleLibraryTracer/Samples.ExampleLibraryTracer.csproj

nuget restore Datadog.Trace.Native.sln

msbuild buildapp.csproj /property:Configuration=Debug /property:Platform=x64 -t:BuildCpp;BuildCppTests


