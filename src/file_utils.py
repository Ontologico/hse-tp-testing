def create_file(path, content):
    with path.open("w") as f:
        f.write(content)


def read_file(path):
    return path.read_text()
