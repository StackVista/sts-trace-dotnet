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
