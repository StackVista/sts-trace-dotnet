rem ls src/**/*.csproj
dotnet restore src/Datadog.Trace.AspNet/Datadog.Trace.AspNet.csproj
dotnet restore src/Datadog.Trace.ClrProfiler.Managed.Core/Datadog.Trace.ClrProfiler.Managed.Core.csproj
dotnet restore src/Datadog.Trace.ClrProfiler.Managed.Loader/Datadog.Trace.ClrProfiler.Managed.Loader.csproj
dotnet restore src/Datadog.Trace.ClrProfiler.Managed/Datadog.Trace.ClrProfiler.Managed.csproj
dotnet restore src/Datadog.Trace.OpenTracing/Datadog.Trace.OpenTracing.csproj
dotnet restore src/Datadog.Trace/Datadog.Trace.csproj

rem ls test/**/*.Tests.csproj
dotnet restore test/Datadog.Trace.ClrProfiler.Managed.Tests/Datadog.Trace.ClrProfiler.Managed.Tests.csproj
dotnet restore test/Datadog.Trace.Tests/Datadog.Trace.Tests.csproj
dotnet restore test/Datadog.Trace.OpenTracing.Tests/Datadog.Trace.OpenTracing.Tests.csproj
