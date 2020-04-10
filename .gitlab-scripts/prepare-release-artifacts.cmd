rem Dirty: address on c# level.

echo Processing x64 msi in OUTCOME\WindowsInstaller\X64\en-us\
pushd OUTCOME\WindowsInstaller\X64\en-us\
ren datadog-* stackstate-*
popd

echo Processing x86 msi in OUTCOME\WindowsInstaller\X64\en-us\
pushd OUTCOME\\WindowsInstaller\X86\en-us\
ren datadog-* stackstate-*
popd

echo Processing Nupkg
pushd OUTCOME\Nupkg\Release
ren datadog-* stackstate.*
popd

echo Processing OpenNupkg
pushd OUTCOME\OpenNupkg\Release
ren datadog-* stackstate.*
popd