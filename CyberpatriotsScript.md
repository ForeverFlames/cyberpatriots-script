# Linux Cybersecurity Checklist for CyberPatriots

This document provides a comprehensive checklist to identify and fix cybersecurity vulnerabilities in Linux systems. Each section addresses specific issues and offers commands to remediate them.

---

## General System Configuration

1. **Update the System**
   - Update all packages to ensure the latest security patches are applied:
     ```bash
     sudo apt-get update && sudo apt-get upgrade -y
     sudo apt-get dist-upgrade -y
     sudo apt-get autoremove -y
     ```
   - Verify installed kernel versions and remove unused ones:
     ```bash
     uname -r
     sudo apt-get remove --purge <old_kernel_version>
     ```

2. **Check for and Remove Unnecessary Software**
   - List all installed packages:
     ```bash
     dpkg --get-selections
     ```
   - Remove unneeded software:
     ```bash
     sudo apt-get purge <package_name>
     ```

3. **Set System Time**
   - Synchronize system time with an NTP server:
     ```bash
     sudo timedatectl set-ntp true
     ```

4. **Enable Automatic Updates**
   - Configure unattended-upgrades:
     ```bash
     sudo apt-get install unattended-upgrades
     sudo dpkg-reconfigure -plow unattended-upgrades
     ```

---

## Account and Authentication Security

1. **Verify User Accounts**
   - List all user accounts:
     ```bash
     cut -d: -f1 /etc/passwd
     ```
   - Lock suspicious accounts:
     ```bash
     sudo usermod -L <username>
     ```

2. **Disable Root Login**
   - Edit `/etc/ssh/sshd_config` and set:
     ```
     PermitRootLogin no
     ```
   - Restart SSH service:
     ```bash
     sudo systemctl restart ssh
     ```

3. **Enforce Password Policy**
   - Edit `/etc/pam.d/common-password`:
     ```
     password requisite pam_pwquality.so retry=3 minlen=12 dcredit=-1 ucredit=-1 ocredit=-1 lcredit=-1
     ```
   - Lock user accounts after failed login attempts:
     ```bash
     echo "auth required pam_tally2.so deny=5 unlock_time=900" | sudo tee -a /etc/pam.d/common-auth
     ```

4. **Disable Guest Accounts**
   - Edit `/etc/lightdm/lightdm.conf`:
     ```
     [SeatDefaults]
     allow-guest=false
     ```

---

## Firewall and Network Security

1. **Enable UFW (Uncomplicated Firewall)**
   - Configure and enable the firewall:
     ```bash
     sudo ufw default deny incoming
     sudo ufw default allow outgoing
     sudo ufw allow ssh
     sudo ufw enable
     ```

2. **Disable IPv6 if Not Needed**
   - Add the following to `/etc/sysctl.conf`:
     ```
     net.ipv6.conf.all.disable_ipv6 = 1
     net.ipv6.conf.default.disable_ipv6 = 1
     ```
   - Apply the changes:
     ```bash
     sudo sysctl -p
     ```

3. **Configure Advanced iptables Rules**
   - Block unnecessary ports and protocols:
     ```bash
     sudo iptables -A INPUT -p tcp --dport 80 -j DROP
     sudo iptables-save | sudo tee /etc/iptables/rules.v4
     ```

---

## File and Directory Permissions

1. **Check File Permissions**
   - Search for world-writable files:
     ```bash
     sudo find / -type f -perm /o+w
     ```
   - Fix permissions:
     ```bash
     sudo chmod o-w <file>
     ```

2. **Verify SUID/SGID Files**
   - List all SUID/SGID files:
     ```bash
     sudo find / -perm /6000
     ```
   - Remove unnecessary SUID/SGID permissions:
     ```bash
     sudo chmod -s <file>
     ```

3. **Audit Home Directory Permissions**
   - Ensure home directories are not world-readable:
     ```bash
     sudo chmod 700 /home/*
     ```

---

## System Logs and Auditing

1. **Enable and Configure Auditd**
   - Install and enable Auditd:
     ```bash
     sudo apt-get install auditd
     sudo systemctl enable auditd
     sudo systemctl start auditd
     ```
   - Review logs:
     ```bash
     sudo ausearch -c <command>
     sudo aureport
     ```

2. **Monitor Login Activity**
   - Check last login attempts:
     ```bash
     last
     ```
   - Monitor failed login attempts:
     ```bash
     sudo cat /var/log/auth.log | grep "Failed password"
     ```

3. **Log Monitoring Tools**
   - Install Logwatch:
     ```bash
     sudo apt-get install logwatch
     ```
   - Run a report:
     ```bash
     sudo logwatch --detail high --mailto <email> --range today
     ```

---

## Advanced Security Configurations

1. **Install Rootkit Detection Tools**
   - Use rkhunter and chkrootkit:
     ```bash
     sudo apt-get install rkhunter chkrootkit
     sudo rkhunter --check
     sudo chkrootkit
     ```

2. **Enable SELinux or AppArmor**
   - Configure SELinux:
     ```bash
     sudo apt-get install selinux-utils selinux-basics
     sudo selinux-activate
     ```
   - Enable AppArmor:
     ```bash
     sudo systemctl enable apparmor
     ```

3. **Disable Unused Filesystems**
   - Add the following to `/etc/modprobe.d/blacklist.conf`:
     ```
     install cramfs /bin/true
     install freevxfs /bin/true
     install jffs2 /bin/true
     ```

4. **Install and Use Lynis**
   - Install Lynis:
     ```bash
     sudo apt-get install lynis
     ```
   - Run an audit:
     ```bash
     sudo lynis audit system
     ```

5. **Configure Login Banners**
   - Add a warning message in `/etc/motd` and `/etc/issue`:
     ```
     Unauthorized access to this system is prohibited.
     ```

---

## Miscellaneous Enhancements

1. **Check for Open Ports**
   - Use `netstat` or `ss`:
     ```bash
     sudo ss -tuln
     ```

2. **Disable USB Ports (If Not Needed)**
   - Add the following to `/etc/modprobe.d/blacklist.conf`:
     ```
     blacklist usb-storage
     ```

3. **Enable Disk Encryption**
   - Verify encryption:
     ```bash
     lsblk
     ```
   - Install and configure LUKS if necessary:
     ```bash
     sudo apt-get install cryptsetup
     ```

4. **Ensure Secure Boot is Enabled**
   - Verify Secure Boot status:
     ```bash
     mokutil --sb-state
     ```

---

This checklist is designed to be comprehensive and should help secure Linux systems while maximizing points in CyberPatriots competitions.
