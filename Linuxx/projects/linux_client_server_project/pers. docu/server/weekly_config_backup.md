# Weekly Config Backup

For now this file is a straight copy from [Latteflo's repo](https://github.com/Latteflo/linux_server)

It's currently midnight and I have no idea what is going on in her config.\
I have subpar development skills so there is no way that I will learn how this work right now, so I'm putting this here as a reference so that I can reflect on it tomorrow and make my own solution.

Thank you for your understanding.

**Changes I'd like to implement**:
- Have multiple backups for all the services, not just glpi.
- not remove backups older than 30 days or at the very least put those in a separate dir like an archive for example.

Backup Configuration Files
Let's create our script in /usr/local/bin/backup_glpi.sh:

sudo nano /usr/local/bin/backup_glpi.sh
Inside the script, we have the following content:
```
#!/bin/bash
# Define backup paths
BACKUP_DIR="/var/backups/glpi"
GLPI_DIR="/var/www/html/glpi"
DB_NAME="glpi"
DB_USER="admin"
DB_PASSWORD="kamkar" 
DATE=$(date +%Y-%m-%d)

# Create a new directory for today's backup
mkdir -p "${BACKUP_DIR}/${DATE}"

# Backup GLPI files
tar -czf "${BACKUP_DIR}/${DATE}/glpi_files_${DATE}.tar.gz" -C "${GLPI_DIR}" .

# Backup GLPI database
mysqldump -u "${DB_USER}" -p"${DB_PASSWORD}" "${DB_NAME}" > "${BACKUP_DIR}/${DATE}/glpi_db_${DATE}.sql"

# Remove backups older than 30 days
find "${BACKUP_DIR}" -type f -mtime +30 -exec rm {} \;
alt text Make the script executable:
```
sudo chmod +x /usr/local/bin/backup_glpi.sh
We can schedule the backup script to run weekly using a cron job.

sudo crontab -e
Add this line to execute the script every Sunday at 2 AM:\
`0 2 * * Sun /usr/local/bin/backup_glpi.sh`\
Annd we save!

The backup script will now run weekly, and we should see the backup files within /var/backups/glpi dated for each week.