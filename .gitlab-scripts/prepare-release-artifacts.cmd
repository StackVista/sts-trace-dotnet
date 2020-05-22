rem Dirty: address on c# level.

echo Processing x64 msi in OUTCOME\WindowsInstaller\X64\en-us\
pushd OUTCOME\WindowsInstaller\X64\en-us\
IF EXIST "datadog-*" (
ren datadog-* stackstate-*
)
popd

echo Processing x86 msi in OUTCOME\WindowsInstaller\X64\en-us\
pushd OUTCOME\WindowsInstaller\X86\en-us\
IF EXIST "datadog-*" (
ren datadog-* stackstate-*
)
popd

echo Processing Nupkg
pushd OUTCOME\Nupkg\Release

IF EXIST "datadog.*" (
ren datadog.* stackstate.*
)

popd

echo Processing OpenNupkg
pushd OUTCOME\OpenNupkg\Release

IF EXIST "datadog.*" (
ren datadog.* stackstate.*
)

popd