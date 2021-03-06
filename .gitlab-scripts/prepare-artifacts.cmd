IF EXIST OUTCOME RMDIR /S /Q OUTCOME
mkdir OUTCOME
mkdir OUTCOME\WindowsInstaller\X64
mkdir OUTCOME\WindowsInstaller\X86
mkdir OUTCOME\Nupkg\
mkdir OUTCOME\OpenNupkg\

xcopy deploy\Datadog.Trace.ClrProfiler.WindowsInstaller\bin\Release\x64\* OUTCOME\WindowsInstaller\X64 /s /e
xcopy deploy\Datadog.Trace.ClrProfiler.WindowsInstaller\bin\Release\x86\* OUTCOME\WindowsInstaller\X86 /s /e
xcopy src\Datadog.Trace\bin\* OUTCOME\Nupkg /s /e
xcopy src\Datadog.Trace.OpenTracing\bin\* OUTCOME\OpenNupkg /s /e
xcopy src\bin\tracer-home.zip OUTCOME\