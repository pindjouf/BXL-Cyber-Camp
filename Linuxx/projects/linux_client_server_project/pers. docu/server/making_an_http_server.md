# How to make an http server with mariadb & GLPI

### Okay so for the setup.

I'm gonna need:

1. **Apache & PHP**\
`sudo apt install php libapache2-mod-php`\
`sudo systemctl restart apache2.service`\
`sudo ufw allow 80`\
And now we can see the beautiful apache default page!\
![alt text](/assets/apache_greeting.png "Title")
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

But we're just gonna run the install script in cli.\
First we have to set permissions:\
`sudo chown -R www-data:www-data /var/www/glpi`\
then\
`php /var/www/glpi/bin/console db:install --db-host=localhost --db-name=glpi --db-user=admin --db-password='water'`

OK so we're missing some mandatory system requirements and some php extensions so let's check that out here's the error fyi:
```
PHP Warning:  Missing required intl PHP extension in /var/www/glpi/src/Session.php on line 747
Some mandatory system requirements are missing. Run the "php bin/console system:check_requirements" command for more details.
```

So I do `sudo php /var/www/glpi/bin/console system:check_requirements`\
And they tell me:
`PHP Warning:  Missing required intl PHP extension in /var/www/glpi/src/Session.php on line 747
Uncaught Exception Error: Class "Normalizer" not found in /var/www/glpi/vendor/symfony/console/Helper/Helper.php at line 65`

I will take care of the intl extension first since I know how to do it.

`sudo vim /etc/php/8.1/apache2/php.ini`
`sudo vim /etc/php/8.1/cli/php.ini`

And uncomment the necessary extensions `intl` in our case. I also took the liberty of uncommenting `mysqli` `curl` & `gd` since I've already had problems with those in the past.

Now when I check requirements I'm getting an even fatter error:
```
PHP Warning:  PHP Startup: Unable to load dynamic library 'curl' (tried: /usr/lib/php/20210902/curl (/usr/lib/php/20210902/curl: cannot open shared object file: No such file or directory), /usr/lib/php/20210902/curl.so (/usr/lib/php/20210902/curl.so: cannot open shared object file: No such file or directory)) in Unknown on line 0
PHP Warning:  PHP Startup: Unable to load dynamic library 'gd' (tried: /usr/lib/php/20210902/gd (/usr/lib/php/20210902/gd: cannot open shared object file: No such file or directory), /usr/lib/php/20210902/gd.so (/usr/lib/php/20210902/gd.so: cannot open shared object file: No such file or directory)) in Unknown on line 0
PHP Warning:  PHP Startup: Unable to load dynamic library 'intl' (tried: /usr/lib/php/20210902/intl (/usr/lib/php/20210902/intl: cannot open shared object file: No such file or directory), /usr/lib/php/20210902/intl.so (/usr/lib/php/20210902/intl.so: cannot open shared object file: No such file or directory)) in Unknown on line 0
PHP Warning:  PHP Startup: Unable to load dynamic library 'mysqli' (tried: /usr/lib/php/20210902/mysqli (/usr/lib/php/20210902/mysqli: cannot open shared object file: No such file or directory), /usr/lib/php/20210902/mysqli.so (/usr/lib/php/20210902/mysqli.so: cannot open shared object file: No such file or directory)) in Unknown on line 0
PHP Warning:  Missing required intl PHP extension in /var/www/glpi/src/Session.php on line 747
Uncaught Exception Error: Class "Normalizer" not found in /var/www/glpi/vendor/symfony/console/Helper/Helper.php at line 65
```

perhaps those extensions weren't installed properly with my php so I have to do it myself.

Here is how I will install them:
```
sudo apt install -y vim wget tar php-curl php-zip php-gd php-intl php-intl php-pear php-imagick php-imap php-memcache php-pspell php-tidy php-xmlrpc php-xsl php-mbstring php-ldap php-ldap php-cas php-apcu libapache2-mod-php php-mysql php-bz2
```

Errors upon errors now.\
My package manager won't update or install anything.

### A few days later...

I've managed to install the missing packages. How, you might ask. Well it just started working for some reason.

This document serves as a testament to my current understanding of the subject.

