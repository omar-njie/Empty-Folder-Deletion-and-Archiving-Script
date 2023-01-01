import os
import getpass

# Get the current user's username
USERNAME = getpass.getuser()

documents_dir = f'/Users/{USERNAME}/Documents'
deleted_folder = f'/Users/{USERNAME}/Desktop/deleted'


def delete_empty_folders(directory):
    """Deletes empty directories in the specified directory and moves them
    to a new folder called "deleted" on the
    desktop.
    """

    if not os.path.exists(deleted_folder):
        os.makedirs(deleted_folder)

    # Iterate over the contents of the user's Documents directory
    for entry in os.scandir(documents_dir):
        if entry.is_dir():
            if not os.listdir(entry.path):
                # Move the empty directory to the "deleted" folder
                os.rename(entry.path, os.path.join(deleted_folder, entry.name))


if __name__ == '__main__':
    # Delete empty folders and move them to the "deleted" folder
    delete_empty_folders(documents_dir)
