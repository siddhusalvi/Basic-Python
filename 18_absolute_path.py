import os
def get_absolute_path(fname):
        return os.path.abspath(fname)


file = "runtime.py"    
print("Absolute path of : ",file,"is",get_absolute_path(file))
