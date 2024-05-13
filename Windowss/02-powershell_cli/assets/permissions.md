# Powershell Permissions

Now that we can navigate and create files, we should be able to change permissions on these. We will use the commands `Get-Acl`, `Set-Acl`, `RunAs`

- Create a file
    - `ni file`
- Check the owner and the groups
    - `Get-Acl file`
- Change the file owner to the built-in administrator (administrator account is disabled by default, check how to enable it. Don't forget to set a strong password!)
    - To active admin account go in cmd and do `net user amdinistrator /active:yes` 
        - d
- Check the file's permission
    - `Get-Acl file`
- Try to print the content of the file as your normal user
    - 
- Print the content of the file using administrator account
    - You have to launch powershell as admin by right-clicking on it. Once you're in `ls `
> **WARNING**: This exercise **will only work on Windows** system since file system permissions are not managed the same way on Windows and Linux.