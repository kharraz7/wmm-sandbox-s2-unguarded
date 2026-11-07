ALLOWED_EXT = {".png", ".jpg", ".pdf"}


def save(name, data):
    import os
    if os.path.splitext(name)[1] not in ALLOWED_EXT:
        raise ValueError("extension not allowed")
    open(name, "wb").write(data)
