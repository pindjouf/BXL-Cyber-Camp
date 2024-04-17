# Powershell Package Management

It's time to start installing softwares and keep them updated. We will see how to use Chocolatey and how to use Windows Updates.

* Instructions

- Get Windows updates
    - Install the `PSWindowsUpdate` module
        - `Install-Module -Name PSWindowsUpdate -RequiredVersion 2.2.0.3`
    - Type `Get-WindowsUpdate` to check for updates
        - 
    - Type `Install-WindowsUpdate` to install updates
- Manage Packages
    - Install `Chocolatey`
    - Install `VLC` from `Chocolatey`
        - `choco install`
    - Upgrade `VLC` to the latest version (it should already be but it's your first use)
        - `choco upgrade`
    - Remove the `VLC` package using `Chocolatey`
        - `choco uninstall`
    - Could you use `Chocolatey` on already installed software? How?
- Manage Windows Features
    - Get installed windows features with the command `Get-WindowsFeature`
    - Install a new feature such as hyper-v with `Install-WindowsFeature`

> **WARGNING**: This exercise **will only work on Windows** since it's specific to the way windows manages packages.