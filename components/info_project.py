def get_info_project(home_path):
    print("""
1.- Projects info
2.- SSH keys info
3.- System info
    """)
    input_option = input(": ")

    if(input_option == '1'):
        print("Project Info")
    elif(input_option == '2'):
        print("SSH Keys Info")
    elif(input_option == '3'):
        print("HOME PATH: ", home_path)
        print("COMMANDS PROJECT: ", )
    print("home_path: ", home_path)
