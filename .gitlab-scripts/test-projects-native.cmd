

call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\Tools\VsDevCmd.bat"
rem Build C++ projects

rem The native profiler depends on the Datadog.Trace.ClrProfiler.Managed.Loader C# project so be sure that is built first
msbuild Datadog.Trace.proj /t:BuildCpp;BuildCppTests /p:Configuration=Release;Platform=x64
msbuild Datadog.Trace.proj /t:BuildCpp;BuildCppTests /p:Configuration=Release;Platform=x86


Datadog.Trace.ClrProfiler.Native.Tests.exe --gtest_output=xml
rem  workingDirectory: $(System.DefaultWorkingDirectory)/test/Datadog.Trace.ClrProfiler.Native.Tests/bin/$(buildConfiguration)/$(buildPlatform)

echo "x64 tests"
pushd %CI_PROJECT_DIR%\test\Datadog.Trace.ClrProfiler.Native.Tests\bin\Release\x64\
Datadog.Trace.ClrProfiler.Native.Tests.exe --gtest_output=xml
popd

echo "x86 tests"
pushd %CI_PROJECT_DIR%\test\Datadog.Trace.ClrProfiler.Native.Tests\bin\Release\x86\
Datadog.Trace.ClrProfiler.Native.Tests.exe --gtest_output=xml
popd



rem testResultsFiles: test/**/test*.xml
