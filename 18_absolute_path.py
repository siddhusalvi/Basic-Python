import os


def get_absolute_path(filename):
    return os.path.abspath(filename)


file = "runtime.py"
print("Absolute path of : ", file, "is", get_absolute_path(file))
