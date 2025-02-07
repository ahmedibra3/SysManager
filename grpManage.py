import subprocess

class GroupManager:
    @staticmethod
    def execute_command(command):
        try:
            result = subprocess.run(command, shell=True, text=True, capture_output=True, check=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.stderr}")

    def add_group(self, advanced=False):
        """
        Adds a new group to the system. Supports both normal and advanced modes.
        """
        groupname = input("Enter the group name to add: ")

        if advanced:
            gid = input("Enter GID (leave empty for default): ") or None
            system_group = input("Is this a system group? (y/n, default: n): ").strip().lower() == 'y'
        else:
            gid = None
            system_group = False

        options = ""
        if gid:
            options += f" -g {gid}"
        if system_group:
            options += " -r"

        self.execute_command(f"sudo groupadd {options} {groupname}")
        print(f"Group '{groupname}' added successfully!")

    def delete_group(self, advanced=False):
        """
        Deletes an existing group. Supports both normal and advanced modes.
        """
        groupname = input("Enter the group name to delete: ")

        if advanced:
            force = input("Force delete group? (y/n, default: n): ").strip().lower() == 'y'
        else:
            force = False

        options = ""
        if force:
            options += " -f"

        self.execute_command(f"sudo groupdel {options} {groupname}")
        print(f"Group '{groupname}' deleted successfully!")

    def list_groups(self):
        """
        Lists all groups in the system.
        """
        self.execute_command("awk -F: '{ if ($3 >= 1000 && $3 < 60000) print $1 }' /etc/group")
