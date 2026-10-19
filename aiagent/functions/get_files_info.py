import os

def get_files_info(working_directory, directory = "."):
    try:
        ab_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(ab_path, directory))
        valid_target_dir = os.path.commonpath([ab_path, target_dir]) == ab_path
        files_info = []
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        elif not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        else:
            for file in os.listdir(target_dir):
                file_path = os.path.join(target_dir, file)
                is_dir = os.path.isdir(file_path)
                file_size = os.path.getsize(file_path)
                result = f"- {file}: file_size={file_size} bytes, is_dir={is_dir}"
                files_info.append(result)
            edited_result = "\n".join(files_info)
            return edited_result
    except Exception as e:
        return f"Error: {e}"
