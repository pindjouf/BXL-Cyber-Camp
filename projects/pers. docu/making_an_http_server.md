# How to make an http server with mariadb & GLPI

### Okay so for the setup.

I'm gonna need:

1. **Apache & PHP**\
`sudo apt install php libapache2-mod-php`\
`sudo systemctl restart apache2.service`\
`sudo ufw allow 80`\
And now we can see the beautiful apache default page!\
[insert apache default page here]
2. **mariadb**\
`sudo apt install mariadb-server`\
`sudo systemctl start mysql`\
`sudo systemctl status mysql`\
And we can see that it's running perfectly fine:
```
● mariadb.service - MariaDB 10.6.16 database server
     Loaded: loaded (/lib/systemd/system/mariadb.service; enabled; vendor preset: enabled)
     Active: active (running) since Thu 2024-04-04 20:43:04 UTC; 16s ago
       Docs: man:mariadbd(8)
```
3. **GLPI**\
My machine crashed so I restarted it.\
Since the new boot I've been unable to ssh into it so everything I say from now on will hypothetical.\
Wait no I just realized it is my firewall blocking my ssh connection, since when I made it I hadn't opened port 22.
I just don't understand why it took so long to apply.\
We're good to go!\
`wget https://github.com/glpi-project/glpi/releases/download/10.0.14/glpi-10.0.14.tgz`\
`tar -xvf glpi-10.0.14.tgz`\
Now let's make a server config for it:\
`sudo vim /etc/apache2/sites-available/default-glpi.conf`\
I'll be using the default config from the glpi docs. This is what it looks like:
```
<VirtualHost *:80>
    ServerName glpi.localhost

    DocumentRoot /var/www/glpi/public

    # If you want to place GLPI in a subfolder of your site (e.g. your virtual host is serving multiple applications),
    # you can use an Alias directive. If you do this, the DocumentRoot directive MUST NOT target the GLPI directory itself.
    # Alias "/glpi" "/var/www/glpi/public"

    <Directory /var/www/glpi/public>
        Require all granted

        RewriteEngine On

        # Ensure authorization headers are passed to PHP.
        # Some Apache configurations may filter them and break usage of API, CalDAV, ...
        RewriteCond %{HTTP:Authorization} ^(.+)$
        RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]

        # Redirect all requests to GLPI router, unless file exists.
        RewriteCond %{REQUEST_FILENAME} !-f
        RewriteRule ^(.*)$ index.php [QSA,L]
    </Directory>
</VirtualHost>
```

Now don't forget to `sudo a2enmod rewrite` to use mod_rewrite since it is in the official default config. Restart apache for the change to take effect.

Now we make a link to it in the `sites-enabled` dir like so:\
`sudo ln -s /etc/apache2/sites-available/default-glpi.conf /etc/apache2/sites-enabled`

And don't forget to remove all the other files in the sites-enabled dir or apache might get confused. And restart apache.

Now apache's gonna be looking for the glpi website on /var/www/glpi. So go ahead and put it there:\
`sudo mv glpi /var/www`\

Your server's IP should now show you the GLPI GUI setup!\
![alt text](/assets/glpi_setup_greeting.png "Title")
