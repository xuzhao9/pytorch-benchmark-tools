import subprocess

class TritonRepo:
    def __init__(self):
        super().__init__(self)
        self._repo_url = "https://github.com/triton-lang/triton.git"

    def build(self):
        build_cmd = ["pip", "install", "-e", "python"]
        subprocess.check_output(build_cmd, cwd=self._repo_dir)
