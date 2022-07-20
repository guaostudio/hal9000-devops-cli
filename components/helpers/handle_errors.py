cli_commands = [
    {
        "name": "ssh_key",
        "arguments_length": [1, 4],
        "arguments": ["--name", "--project-type"]
    }
]


def handle_parameters_errors(cli_command, arguments_data):
    for command in cli_commands:
        if(command["name"] == cli_command):
            for argument_length in command["arguments_length"]:
                if(len(arguments_data) == argument_length):
                    return {
                        "success": True,
                        "data": arguments_data_to_object(arguments_data, command["arguments"])
                    }

        for argument in command["arguments"]:
            if(argument not in arguments_data):
                print("Error: The argument '{}' is missing".format(argument))
                return {
                    "success": False,
                    "data":  arguments_data_to_object(arguments_data, command["arguments"])
                }
        return {
            "success": True,
            "data":  arguments_data_to_object(arguments_data, command["arguments"])
        }


def arguments_data_to_object(data, valid_arguments):
    arguments_data = {}

    for index, arg_data in enumerate(data):
        for valid_arg in valid_arguments:
            if(arg_data == valid_arg):
                arguments_data[data[index].replace("-", "")] = data[index + 1]

    return arguments_data
