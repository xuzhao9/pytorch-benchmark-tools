import subprocess

class Repo:
    def __init__(self):
        pass

    def checkout(self):
        cmd = ["git", "clone", self._repo_url]
        subprocess.check_call(cmd)
    
    def checkout_commit(self, commit):
        cmd = ["git", "checkout", commit]
        subprocess.check_call(cmd)
        checkout_submodules = ["git", "submodules", "update", "--init", "--recursive"]
        subprocess.check_call(checkout_submodules)
