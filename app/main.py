def copy_file(command: str) -> None:
    if not command.lower().startswith("cp"):
        return
    files = [
        file
        for file in command.split()
        if file.lower().endswith(".txt")
    ]
    if len(files) < 2:
        return
    file_1 = files[0]
    file_2 = files[1]
    if file_1 != file_2:
        try:
            with open(file_1, "r") as f:
                content = f.read()
            with open(file_2, "w") as newf:
                newf.write(content)
        except FileNotFoundError:
            pass
