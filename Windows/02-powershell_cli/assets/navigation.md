# Powershell Navigation

Now we will learn how to move around in the filesystem with `Set-Location`, `Get-Location`, `Get-ChildItem` ...

- Print your current location on the screen
    - `Get-Location` OR `pwd`
- Print the content of your current directory
    - `Get-ChildItem` OR `ls` 
- Print the content of your root (`C:` _if you're running windows_, `/` _for linux_)
    - `Get-ChildItem C:\` OR `ls C:\`
- Go into your home folder (_C:\Users\Username or /home/Username_)
    - `Set-Location ~` OR `cd ~`
- Print the content of your home
    - `Get-ChildItem ~` OR `ls ~`
- Those commands are pretty long to type, do you know any shorter way to do it?
    - Yes, we can use their aliases i.e. the habitual linux commands, like I've outlined above.