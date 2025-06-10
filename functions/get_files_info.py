import os

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
