import os
import ast
import sys

def search_functions_in_file(file_path, function_name):
    with open(file_path, "r") as file:
        content = file.read()
        try:
            parsed_ast = ast.parse(content)
            for node in ast.walk(parsed_ast):
                if isinstance(node, ast.FunctionDef) and node.name == function_name:
                    return True
        except SyntaxError:
            pass
    return False

def search_and_import_functions(directory, function_name):
    current_script_name = os.path.basename(sys.argv[0])
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file != current_script_name and file.endswith(".py"):
                file_path = os.path.join(root, file)
                if search_functions_in_file(file_path, function_name):
                    print(f"Function '{function_name}' found in '{file_path}'")

# Specify the directory and function name
directory_path = "/path/to/your/directory"
function_to_search = "your_function_name"

search_and_import_functions(directory_path, function_to_search)