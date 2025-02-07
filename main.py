import usrManage,grpManage

class Menu:
    def __init__(self):
        self.user_manager = usrManage.UserManager()
        self.group_manager = grpManage.GroupManager()

    def display_menu(self):
        more = 'y'
        while more == 'y':
            print(
                """
===============================================================  | ================================================================
|                             |                               |  | |                             |                                |
|      OPERATIONS(USERs)      |         PREES NUMBER          |  | |      OPERATIONS(GROUPs)     |         PREES NUMBER           |
|                             |                               |  | |                             |                                |
|=============================================================|  | |==============================================================|
|  Add User                   |                1              |  | |  Add Group                  |                8               |
|=============================================================|  | |==============================================================|
|  Modify User                |                2              |  | |  Delete Group               |                9               |
|=============================================================|  | |==============================================================|
|  Delete User                |                3              |  | |  List Groups                |                10              |
|=============================================================|  | |==============================================================|
|  List Users                 |                4              |  |
|=============================================================|  |
|  Disable User               |                5              |  |
|=============================================================|  |
|  Enable User                |                6              |  |
|=============================================================|  |
|  Change Password            |                7              |  |
|=============================================================|  |


                                    |====================================================================|
                                    |  About                   |                11                       |
                                    |====================================================================|
                                    |  Exit                    |                12                       |
                                    |====================================================================|
    """)
            choice = input("Enter your choice: ")

            if choice == "1":
                advanced = input("Advanced mode? (y/n, default: n): ").strip().lower() == 'y'
                self.user_manager.add_user(advanced)
            elif choice == "2":
                advanced = input("Advanced mode? (y/n, default: n): ").strip().lower() == 'y'
                self.user_manager.modify_user(advanced)
            elif choice == "3":
                advanced = input("Advanced mode? (y/n, default: n): ").strip().lower() == 'y'
                self.user_manager.delete_user(advanced)
            elif choice == "4":
                self.user_manager.list_users()
            elif choice == "5":
                advanced = input("Advanced mode? (y/n, default: n): ").strip().lower() == 'y'
                self.user_manager.disable_user()
            elif choice == "6":
                advanced = input("Advanced mode? (y/n, default: n): ").strip().lower() == 'y'
                self.user_manager.enable_user()
            elif choice == "7":
                self.user_manager.change_password()
            elif choice == "8":
                self.group_manager.add_group(advanced)
            elif choice == "9":
                self.group_manager.delete_group(advanced)
            elif choice == "10":
                self.group_manager.list_groups()
            elif choice == "11":
                print("This script allows user and group management in CentOS Stream 9.")
            elif choice == "12":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
            
            more = input("Do you do more operations?(y/n): default n: ").strip().lower()
            if more != 'y':
                print("Exiting...")
                break



if __name__ == "__main__":
    menu = Menu()
    menu.display_menu()
