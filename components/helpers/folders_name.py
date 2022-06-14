def folders_name():
    folders = []

    api = input("Do you have a API repository? (y/n): ")
    if api == "y" or api == "Y":
        folders.append("api")

    admin = input("Do you have a ADMIN repository? (y/n): ")
    if admin == "y" or admin == "Y":
        folders.append("admin")

    page = input("Do you have a PAGE repository? (y/n): ")
    if page == "y" or page == "Y":
        folders.append("page")

    other = input("Do you have a other repository? (y/n): ")
    while other == "y" or other == "Y":
        folder = input("\nWhat is the name of the folder?: ")
        folders.append(folder)

        continue_add_folders = input("Do you want to add more folders? (y/n) ")
        if continue_add_folders == "n" or continue_add_folders == "N":
            other = "n"

    print("Folders: ", folders)
    return folders
