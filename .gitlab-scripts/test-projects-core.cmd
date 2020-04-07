rem ls test/**/*.Tests.csproj
dotnet test test/Datadog.Trace.ClrProfiler.Managed.Tests/Datadog.Trace.ClrProfiler.Managed.Tests.csproj --configuration %CONFIGURATION%
dotnet test test/Datadog.Trace.Tests/Datadog.Trace.Tests.csproj --configuration %CONFIGURATION%
dotnet test test/Datadog.Trace.OpenTracing.Tests/Datadog.Trace.OpenTracing.Tests.csproj --configuration %CONFIGURATION%
