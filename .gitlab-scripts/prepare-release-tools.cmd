call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\Tools\VsDevCmd.bat"

rem If locally, consider SET CI_PROJECT_DIR=C:\Work\sts-trace-dotnet 
SET SOLUTION_DIR=%CI_PROJECT_DIR%
SET TOOL_BUILD_CONFIG=Release
SET INTEGRATIONS_PROJ=%SOLUTION_DIR%\src\Datadog.Trace.ClrProfiler.Managed\Datadog.Trace.ClrProfiler.Managed.csproj
SET OUTPUT_DIR=%SOLUTION_DIR%\tools\PrepareRelease\bin\tracer-home

dotnet publish %INTEGRATIONS_PROJ% -c %TOOL_BUILD_CONFIG% -f net45 -o "%OUTPUT_DIR%\net45"
dotnet publish %INTEGRATIONS_PROJ% -c %TOOL_BUILD_CONFIG% -f net461 -o "%OUTPUT_DIR%\net461"
dotnet publish %INTEGRATIONS_PROJ% -c %TOOL_BUILD_CONFIG% -f netstandard2.0 -o "%OUTPUT_DIR%\netstandard2.0"

echo Look for artifacts in %SOLUTION_DIR%\tools\PrepareRelease\bin\tracer-home