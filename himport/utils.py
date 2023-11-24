import os
import atexit
from sys import platform

class TemporaryDirectory:
    def __init__(self, name, module_name):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        self.dir = os.path.join(script_dir, name)
        self.module_name = module_name

        if not os.path.exists(self.dir):
            os.makedirs(self.dir)

        @atexit.register
        def remove_temp_dir():
            if os.path.exists(self.dir):
                os.remove(f"hcache/{self.module_name}.py")
                if platform == "linux" or platform == "linux2":
                    os.system("find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete")
                elif platform == "darwin":
                    os.system("find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete")
                elif platform == "win32":
                    os.system("python3 -Bc \"import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]\"")
                    os.system("python3 -Bc \"import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]\"")
                os.removedirs("hcache")

    def __enter__(self):
        return self.dir

    def __exit__(self, exc_type, exc_value, traceback):
        if os.path.exists(self.dir):
            os.removedirs(self.dir)

    def __del__(self):
        if os.path.exists(self.dir):
            os.removedirs(self.dir)