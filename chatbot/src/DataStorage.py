# DataStorage.py

class DataStorage:
    def __init__(self, storage_file):
        self.storage_file = storage_file

    def save_user_info(self, user_info):
        """
        Saves user information to a storage file.
        
        Parameters:
        - user_info (dict): A dictionary containing user information.
        """
        with open(self.storage_file, 'a') as file:
            file.write(','.join(user_info.values()) + '\n')

    def read_user_info(self):
        """
        Reads user information from the storage file.
        
        Returns:
        - list: A list of dictionaries containing user information.
        """
        user_info_list = []
        with open(self.storage_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                user_info = line.strip().split(',')
                user_info_dict = {
                    "name": user_info[0],
                    "phone": user_info[1],
                    "email": user_info[2]
                }
                user_info_list.append(user_info_dict)
        return user_info_list
