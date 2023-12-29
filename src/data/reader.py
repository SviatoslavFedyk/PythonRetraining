import json

def read_json_file(file_path,serializer):
    with open(file_path, "r") as f:
        data = json.loads(f.read())
    return serializer(data)