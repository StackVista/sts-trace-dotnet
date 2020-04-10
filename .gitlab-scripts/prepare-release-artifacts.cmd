rem Dirty: address on c# level.

pushd OUTCOME\WindowsInstaller\X64\en-us\
ren datadog-* stackstate-*
popd

pushd OUTCOME\\WindowsInstaller\X86\en-us\
ren datadog-* stackstate-*
popd

pushd OUTCOME\Nupkg\Release
ren datadog-* stackstate-*
popd

pushd OUTCOME\OpenNupkg\Release
ren datadog-* stackstate-*
popd