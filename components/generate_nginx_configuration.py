import os

nginx_multi_config_path = "/home/ubuntu/templates/nginx_multiple_files_config.txt"
nginx_a_config_path = "/home/ubuntu/templates/nginx_one_file_config.txt"


def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


def nginx_config():
    resume = "y"

    while resume == "y" or resume == "Y":
        print("Generate a new nginx file")
        print(
            "1. 1 file (api, admin, page in a file | routes page.com/admin | page.com/api)")
        print("2. 3 file (api, admin, page in multiple files | routes admin.page.com | api.page.com)")
        print("3. Start certbot")
        print("99. Exit")

        option = input("Select an option: ")

        if option == "1":
            nginx_file = ""

            server_name = input("Enter the server name: ")
            api_port = input("Enter the port of the api: ")
            admin_port = input("Enter the port of the admin: ", api_port)
            page_port = input("Enter the port of the page: ", admin_port)

            with open(nginx_a_config_path, "r") as nginx_config_template:
                nginx_file = nginx_config_template.read()

            nginx_file = nginx_file.replace("{{SERVER_NAME}}", server_name)
            nginx_file = nginx_file.replace("{{PAGE_PORT}}", page_port)
            nginx_file = nginx_file.replace("{{ADMIN_PORT}}", admin_port)
            nginx_file = nginx_file.replace("{{API_PORT}}", api_port)

            with open(server_name + ".conf", "w") as file:
                file.write(nginx_file)
            print("Please allow sudo permissions to move files to /etc/nginx/conf.d/")
            os.system("sudo mv " + server_name + ".conf /etc/nginx/conf.d/")
            clearConsole()

            print(
                "\n NGINX CONFIG FILE WAS GENERATED SUCCESSFULLY AND MOVED TO /etc/nginx/conf.d/")
            resume = "n"

        elif option == "2":
            multiple_files = ["api", "admin", "page"]

            for file in multiple_files:
                file_name = input(f"Do you have a {file}? (y/n):")

                if file_name == "y" or file_name == "Y":
                    nginx_file = ""
                    server_name = input("Enter the server name: ")
                    port = input("Enter the port: ")

                    with open(nginx_multi_config_path, "r") as nginx_config_template:
                        nginx_file = nginx_config_template.read()

                    nginx_file = nginx_file.replace(
                        "{{SERVER_NAME}}", server_name)
                    nginx_file = nginx_file.replace("{{PORT}}", port)

                    with open(f"{file}.{server_name}" + ".conf", "w") as file:
                        file.write(nginx_file)

                    print(
                        "Please allow sudo permissions to move files to /etc/nginx/conf.d/")
                    os.system(
                        "sudo mv " + f"{file}.{server_name}" + ".conf /etc/nginx/conf.d/")
                    clearConsole()

                print(
                    "\n NGINX CONFIG FILE WAS GENERATED SUCCESSFULLY AND MOVED TO /etc/nginx/conf.d/")
                resume = "n"

        elif option == "3":
            os.system("sudo certbot --nginx")
            resume = "n"

        elif option == "99":
            resume = "n"
        else:
            print("Invalid option")
