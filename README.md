# SysManager

# User and Group Management Tool

A Python-based command-line tool for managing users and groups on CentOS. This tool simplifies the administration of user accounts and groups, making it easier for system administrators to perform common tasks like adding, modifying, deleting users, and managing groups.

---

## **Features**
- **User Management**:
  - Add, modify, and delete users.
  - Enable or disable user accounts.
  - Change user passwords securely using hidden input.
  - List all users in the system.
  
- **Group Management**:
  - Add, modify, and delete groups.
  - Assign users to specific groups.
  - List all groups in the system.

- **Secure Operations**:
  - Commands require `sudo` privileges.
  - Password input is masked for security.

---

## **Requirements**
- Python 3.6 or higher.
- CentOS or any Linux-based distribution with the following tools installed:
  - `sudo`
  - `useradd`, `usermod`, `userdel`, `groupadd`, `groupdel`.
- Administrator privileges for running the tool.

---

## **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/ahmedibra3/SysManager.git
