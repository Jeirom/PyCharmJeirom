from mypy.build import json_dumps
import json

def save_file(data, file_path):
    try:
        with open(file_path, 'w') as f:
            json.dump(data, file_path)
    except Exception:
        return []