SET CONFIGURATION=Debug
rem ls src/**/*.csproj
nuget restore Datadog.Trace.sln
dotnet build src/Datadog.Trace.AspNet/Datadog.Trace.AspNet.csproj --configuration %CONFIGURATION%
dotnet build src/Datadog.Trace.ClrProfiler.Managed.Core/Datadog.Trace.ClrProfiler.Managed.Core.csproj --configuration %CONFIGURATION%
dotnet build src/Datadog.Trace.ClrProfiler.Managed.Loader/Datadog.Trace.ClrProfiler.Managed.Loader.csproj --configuration %CONFIGURATION%
dotnet build src/Datadog.Trace.ClrProfiler.Managed/Datadog.Trace.ClrProfiler.Managed.csproj --configuration %CONFIGURATION%
dotnet build src/Datadog.Trace.OpenTracing/Datadog.Trace.OpenTracing.csproj --configuration %CONFIGURATION%
dotnet build src/Datadog.Trace/Datadog.Trace.csproj --configuration %CONFIGURATION%
