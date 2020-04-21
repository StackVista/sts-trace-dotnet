# Windows setup for StackState agent testing.
This guide assumes we are using VirtualBox for running VM.
Get Windows VM from [https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/](https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/])
Run it in VirtualBox and install VirtualBox Guest OS Addons.

## Install chocolatey on Windows
Do it in PowerShell as Admin.
```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

## Setup windows
Use chocolatey as Admin in PowerShell.

```
choco install firefox
```
Then set Firefox as default browser in Windows.

```
choco install git 
```
Generate ssh keys and add them to GitHub, GitLab. Setup git username and email.

```
choco install dotnetcore-sdk 
choco install netfx-4.5.2-devpack
choco install vscode 
choco install powershell-core
```

## Build and deploy your project to IIS

If you need Visual Studio do
```
choco install visualstudio2019community
```

Checkout your project with git and build it.
Then deploy it to IIS.

## Install StackState Agent

Install StackState Agent and point it to the simulator running on host machine.
```
. { iwr -useb https://stackstate-agent-2.s3.amazonaws.com/install.ps1 } | iex; install -stsApiKey "API_KEY" -stsUrl "http://HostMachineIP:7078/stsAgent"
```
You can find host machine ip with `ipconfig` command.

## Install .NET Tracer for Datadog APM

Get latest msi `stackstate-net-apm` release from [https://github.com/StackVista/sts-trace-dotnet/releases](https://github.com/StackVista/sts-trace-dotnet/releases)
Install it on Windows VM.

## Run simulator on Host machine

Run docker simulator container.
```
docker run -p 7078:7078 quay.io/stackstate/simulator:master -v record -p 7078 -t tpl.json
```

Download recorder data.
```
curl -o temp.json http://localhost:7078/download
```
