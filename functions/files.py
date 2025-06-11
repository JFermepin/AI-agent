import os
import subprocess

MAX_CHARS = 10000

def get_files_info(working_directory, directory=None):

    full_abs_dir = os.path.abspath(os.path.join(working_directory, directory))
    
    if not (full_abs_dir.startswith(os.path.abspath(working_directory)) or (os.path.abspath(directory) == os.path.abspath(working_directory))):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if os.path.isfile(full_abs_dir):
        return f'Error: "{directory}" is not a directory'
    
    try:
        files_info = []
        for filename in os.listdir(full_abs_dir):
            filepath = os.path.join(full_abs_dir, filename)
            file_size = 0
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    
    except Exception as e:
        return f"Error listing files: {e}"


def get_file_content(working_directory, file_path):
    full_abs_file = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not (full_abs_file.startswith(os.path.abspath(working_directory)) or (os.path.abspath(file_path) == os.path.abspath(working_directory))):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(full_abs_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(full_abs_file, 'r') as file:
            content = file.read(MAX_CHARS)
            if len(content) == MAX_CHARS:
                content += f"...File '{file_path}' truncated at 10000 characters"
        return content
    except Exception as e:
        return f"Error reading file: {e}"
    

def write_file(working_directory, file_path, content):
    full_abs_file = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not (full_abs_file.startswith(os.path.abspath(working_directory)) or (os.path.abspath(file_path) == os.path.abspath(working_directory))):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        with open(full_abs_file, 'w') as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error writing file: {e}"
    

def run_python_file(working_directory, file_path, args=None):
    abs_working_dir = os.path.abspath(working_directory)
    full_abs_file = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not (full_abs_file.startswith(os.path.abspath(working_directory)) or (os.path.abspath(file_path) == os.path.abspath(working_directory))):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(full_abs_file):
        return f'Error: File "{file_path}" not found.'
    
    if not full_abs_file.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
        

    try:
        commands = ["python", full_abs_file]
        if args:
            commands.extend(args)
        result = subprocess.run(
            commands,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=abs_working_dir,
        )
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"
    