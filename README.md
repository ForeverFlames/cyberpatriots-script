# cyberpatriots-script
# Checklist:
# sudo apt-get update && sudo apt-get upgrade
# sudo apt-get install ufw && sudo ufw enable
# sudo apt-get install openssh-server*
# sudo nano /etc/ssh/sshd_config
# PermitRootLogin no
# Updates(Software & Updates < Set Security Updates to daily)
# sudo apt-get install apache2
sudo nano /etc/apache2/conf-available/security.conf
ServerTokens ProductOnly
sudo nano /etc/apache2/apache2.conf
AllowOverride None
RequestReadTimeout header=10-20,MinRate=500 body=20,MinRate=500
TODO: NGINX
TODO: FTP
service –status-all
Remove (UNLESS REQUIRED IN README):
NGINX*
APACHE*
SSH*
VSFTPD (or anything that is ftp related)*
chmod -R 640 /etc/sudoers
chmod -R 640 /etc/group
chmod -R 640 /etc/passwd
chmod -R 640 /etc/shadow
sudo nano /etc/lightdm/lightdm.conf**
allow-guest=false
sudo nano /etc/crontab
Check for anything suspicious
sudo nano /etc/login.defs
Change:
PASS_MAX_DAY 90
PASS_MIN_DAY 10
PASS_WARN_AGE 7
Secure /etc/sysctl****
sudo find . -type f -exec file -N -i -- {} + | sed -n 's!: video/[^:]*$!!p'
Update the Kernel***
User Section:
Remove Unauthorized Users
Add Any Required Users in read-me
Remove permissions from unauthorized admins
Give admin to any user without it that is authorized
Change insecure password(s) of admin(s)





*Depends on the required service
**Only if display manager is lightdm
***Changes between flavors
****#11 on Checklist #3






CHECK NEXT PAGE FOR ADDITIONAL CHECKS
It might not be defined in the README but go through all of the files in the OS system and find some files that seem that they shouldn’t be on the OS system ex. Water bottle .jpeg, mp3 files. Some files may be hidden so you might have to use $ sudo ls -a OR $ ls -a.

DISABLE ROOT LOGIN IN SSH

Disable rsh hosts as they are unencrypted- READ THIS
IgnoreRhosts yes

Check list of installed packages for samba packages
sudo apt list | grep -i samba

Remove all samba related packages- 
sudo apt-get remove .*samba.* .*smb.*

No keepalive/unattended sessions-’
 ClientAliveInterval 300 ClientAliveCountMax 0

Run check on sshd config- 
sudo sshd -t

Run rootkit, backdoor checks- 
sudo apt-get install chkrootkit rkhunter
sudo chkrootkit
sudo rkhunter --update
sudo rkhunter --check

