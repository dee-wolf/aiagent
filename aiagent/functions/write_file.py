import os

def write_file(working_directory, file_path, content):
    try:
        ab_path = os.path.abspath(working_directory)
        target_path =os.path.abspath(os.path.join(ab_path, file_path))
        valid_target_file = os.path.commonpath([ab_path, target_path]) == ab_path
        if not valid_target_file:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        directory = os.path.dirname(target_path)
        os.makedirs(directory, exist_ok=True)
        with open(target_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
