from google.genai import types

# Function schemas for the AI Code Assistant
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns the contents of a file in the specified path (up to 10000 characters), constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "path": types.Schema(
                type=types.Type.STRING,
                description="The path to where the file is, relative to the working directory. If not provided or incorrect, the output will result in an error message.",
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes a file in the specified path with the specified content, constrained to the working directory. If the file doesn't exist, it will be created.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "path": types.Schema(
                type=types.Type.STRING,
                description="The path to where the file is, relative to the working directory. If not provided, the file will be written in the working directory itself.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file and returns its stdoput, stderr and exit code (if its not 0), constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to where the python file is, relative to the working directory. If not provided, the file will be search in the working directory itself. If the file is not a .py file, the output will result in an error message.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="The arguments to pass to the python file when running it. If not provided, the file will be run without any arguments.",
            ),
        },
    ),
)

# Define the available functions for the AI Code Assistant
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
    ]
)