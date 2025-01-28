# Comprehensive Linux Checklist for CyberPatriot

## **General Setup**

### 1. **Read the Readme**
- Take notes on necessary services, users, and other important details.

### 2. **Forensics Questions**
- Answer forensic questions as they often point to vulnerabilities (e.g., hidden messages, backdoors, unauthorized files).

---

## **Account Configuration**

### 1. **Root and Guest Accounts**
- Lock the root account:
  ```bash
  passwd -l root
  ```
- Disable the guest account in `/etc/lightdm/lightdm.conf`:
  ```bash
  allow-guest=false
  greeter-hide-users=true
  greeter-show-manual-login=true
  autologin-user=none
  ```

### 2. **User Management**
- Compare `/etc/passwd` and `/etc/group` to the Readme.
  - Look out for UID 0 and hidden users.
- Delete unauthorized users:
  ```bash
  userdel -r <username>
  groupdel <username>
  ```
- Add authorized users:
  ```bash
  useradd -G <group1>,<group2> <username>
  passwd <username>
  ```
- Manage group memberships:
  ```bash
  gpasswd -d <username> <group>   # Remove from group
  gpasswd -a <username> <group>   # Add to group
  ```
- Verify `/etc/sudoers` and `/etc/sudoers.d` for unauthorized users or groups.
  - Remove `NOPASSWD` and `!authenticate` entries.

---

## **Password Policy**

### 1. **Password Expiration**
- Edit `/etc/login.defs`:
  ```bash
  PASS_MAX_DAYS 30
  PASS_MIN_DAYS 7
  PASS_WARN_AGE 12
  ```

### 2. **Password Complexity**
- Install Cracklib:
  ```bash
  apt-get install libpam-cracklib
  ```
- Edit `/etc/pam.d/common-password`:
  ```bash
  password required pam_unix.so obscure sha512 remember=12 use_authtok
  password required pam_cracklib.so retry=3 minlen=13 difok=4 dcredit=-1 ucredit=-1 ocredit=-1 lcredit=-1 maxrepeat=3
  ```

### 3. **Account Lockout Policy**
- Edit `/etc/pam.d/common-auth`:
  ```bash
  auth required pam_tally2.so deny=5 audit unlock_time=1800 onerr=fail even_deny_root
  ```

### 4. **Change Passwords**
- Update all user passwords:
  ```bash
  passwd <username>
  ```

---

## **Network Security**

### 1. **Firewall Configuration (UFW)**
- Enable and configure UFW:
  ```bash
  ufw default deny incoming
  ufw default allow outgoing
  ufw allow <port/service>
  ufw delete <rule>
  ufw logging on
  ufw logging high
  ufw enable
  ```

### 2. **Host Configuration**
- Check `/etc/hosts` for suspicious entries.
- Prevent IP spoofing:
  ```bash
  echo "nospoof on" >> /etc/host.conf
  ```

### 3. **Secure SSH (if required)**
- Edit `/etc/ssh/sshd_config`:
  ```bash
  PermitRootLogin no
  Protocol 2
  MaxAuthTries 3
  ClientAliveInterval 300
  ClientAliveCountMax 0
  LoginGraceTime 20
  StrictModes yes
  PasswordAuthentication no  # Optional for key-based authentication
  ```
- Restart SSH:
  ```bash
  service sshd restart
  ```

---

## **Package Management**

### 1. **Verify Repositories**
- Check `/etc/apt/sources.list` and apt keys:
  ```bash
  apt-cache policy
  apt-key list
  ```

### 2. **Updates**
- Update and upgrade the system:
  ```bash
  apt-get update
  apt-get -y upgrade
  ```
- Enable automatic updates:
  ```bash
  apt-get install unattended-upgrades
  dpkg-reconfigure unattended-upgrades
  ```
- Configure `/etc/apt/apt.conf.d/20auto-upgrades`:
  ```bash
  APT::Periodic::Update-Package-Lists "1";
  APT::Periodic::Download-Upgradeable-Packages "1";
  APT::Periodic::AutocleanInterval "7";
  APT::Periodic::Unattended-Upgrade "1";
  ```

---

## **Service Management**

### 1. **List and Remove Services**
- List all services:
  ```bash
  service --status-all
  ```
- Remove unnecessary services:
  ```bash
  apt-get purge <service>
  ```

### 2. **Secure Configuration**
- Verify service configuration files (e.g., Apache, SSH, FTP).
- Ensure no default credentials are in use.

---

## **File and Permissions Management**

### 1. **Sensitive Files**
- Verify permissions for sensitive files:
  ```bash
  ls -al /etc/passwd /etc/group /etc/shadow /etc/sudoers /var/www
  chmod -R 640 <file>
  ```

### 2. **Media Files**
- Search for unauthorized media files:
  ```bash
  find / -iname "*.<extension>"
  ls -alR /home
  ```

---

## **Malware and Backdoor Detection**

### 1. **Check for Malware**
- Verify `/etc/rc.local` contains only `exit 0`.
- Check running processes:
  ```bash
  ps -aux
  ```
- Install and run Rootkit Hunter:
  ```bash
  apt-get install rkhunter
  rkhunter --propupd
  rkhunter --checkall
  ```

### 2. **Install ClamAV**
- Install and scan:
  ```bash
  apt-get install clamav
  freshclam
  clamscan -i -r --remove=yes /
  ```

---

## **Notes**
- Assume root permissions for most commands.
- Be cautious with `dist-upgrade` as it may break critical services.
- Use multiple terminals for parallel tasks when possible.

---

This checklist is designed for CyberPatriot Linux Hardening and should be adapted based on specific competition requirements and the Readme instructions provided.
