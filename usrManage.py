import subprocess
from getpass import getpass

class UserManager:
    @staticmethod
    def execute_command(command):
        try:
            result = subprocess.run(command, shell=True, text=True, capture_output=True, check=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.stderr}")

    def add_user(self, advanced=False):
        """
        Adds a new user to the system. Supports both normal and advanced modes.
        """
        username = input("Enter the username to add: ")

        if advanced:
            home_dir = input("Enter home directory (leave empty for default): ") or None
            shell = input("Enter shell (default: /bin/bash): ") or "/bin/bash"
            system_user = input("Is this a system user? (y/n, default: n): ").strip().lower() == 'y'
            no_create_home = input("Do not create home directory? (y/n, default: n): ").strip().lower() == 'y'
            uid = input("Enter UID (leave empty for default): ") or None
            gid = input("Enter GID (Should be existing)(leave empty for default): ") or None
            comment = input("Enter a comment/description (leave empty for none): ") or None
            password = input("Enter a password ")
        else:
            home_dir = None
            shell = "/bin/bash"
            system_user = False
            no_create_home = False
            uid = None
            gid = None
            comment = None
            password = None

        options = []
        if home_dir:
            options.append(f"-d {home_dir}")
        if shell:
            options.append(f"-s {shell}")
        if system_user:
            options.append("-r")
        if no_create_home:
            options.append("--no-create-home")
        else:
            options.append("-m")
        if uid:
            options.append(f"-u {uid}")
        if gid:
            options.append(f"-g {gid}")
        if comment:
            options.append(f"-c \"{comment}\"")
        if password:
            options.append(f" -p $(openssl passwd -6 {password})")

        command = f"sudo useradd {' '.join(options)} {username}"
        self.execute_command(command)
        print(f"User '{username}' added successfully!")

    def modify_user(self, advanced=False):
        """
        Modifies an existing user. Supports both normal and advanced modes.
        """
        username = input("Enter the username to modify: ")

        if advanced:
            new_username = input("Enter new username (leave empty for no change): ") or None
            home_dir = input("Enter new home directory (leave empty for no change): ") or None
            move_home = input("Move home directory? (y/n, default: n): ").strip().lower() == 'y'
            shell = input("Enter new shell (leave empty for no change): ") or None
            uid = input("Enter new UID (leave empty for no change): ") or None
            gid = input("Enter new GID (leave empty for no change): ") or None
            lock = input("Lock the account? (y/n, default: n): ").strip().lower() == 'y'
            unlock = input("Unlock the account? (y/n, default: n): ").strip().lower() == 'y'
            comment = input("Enter new comment/description (leave empty for no change): ") or None
        else:
            new_username = None
            home_dir = None
            move_home = False
            shell = None
            uid = None
            gid = None
            lock = False
            unlock = False
            comment = None

        options = []
        if new_username:
            options.append(f" -l {new_username}")
        if home_dir:
            options.append(f" -d {home_dir}")
            if move_home:
                options.append(" -m")
        if shell:
            options.append(f" -s {shell}")
        if uid:
            options.append(f" -u {uid}")
        if gid:
            options.append(f" -g {gid}")
        if lock:
            options.append(" -L")
        if unlock:
            options.append(" -U")
        if comment:
            options.append(f" -c \"{comment}\"")

        if options:
            command = f"sudo usermod {' '.join(options)} {username}"
            self.execute_command(command)
            print(f"User '{username}' modified successfully!")
        else:
            print("No modification options provided.")

    def delete_user(self, advanced=False):
        """
        Deletes an existing user. Supports both normal and advanced modes.
        """
        username = input("Enter the username to delete: ")

        if advanced:
            remove_home = input("Remove home directory? (y/n, default: n): ").strip().lower() == 'y'
            force = input("Force delete? (y/n, default: n): ").strip().lower() == 'y'
        else:
            remove_home = False
            force = False

        options = []
        if remove_home:
            options.append(" -r")
        if force:
            options.append(" -f")

        command = f"sudo userdel {' '.join(options)} {username}"
        self.execute_command(command)
        print(f"User '{username}' deleted successfully!")

    def list_users(self):
        """
        Lists all users in the system.
        """
        self.execute_command("awk -F: '{ if ($3 >= 1000 && $3 < 60000) print $1 }' /etc/passwd")

    def disable_user(self):
        """
        Locks a user's account.
        """
        username = input("Enter the username to disable: ")
        self.execute_command(f"sudo passwd -l {username}")
        print(f"User '{username}' disabled successfully!")

    def enable_user(self):
        """
        Unlocks a user's account.
        """
        username = input("Enter the username to enable: ")
        self.execute_command(f"sudo passwd -u {username}")
        print(f"User '{username}' enabled successfully!")

    def change_password(self):
        """
        Changes a user's password.
        """
        username = input("Enter the username to change password: ")
        password = getpass("Enter a new password: ")
        self.execute_command(f"echo '{username}:{password}' | sudo chpasswd")
        print(f"Password of '{username}' updated successfully!")

