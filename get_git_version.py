import subprocess

def get_git_commit_hash():
    try:
        commit_hash = subprocess.check_output(
            ['git', 'rev-parse', 'HEAD'],
            stderr=subprocess.STDOUT
        ).strip().decode('utf-8')
        return commit_hash
    except Exception:
        return "unknown"


if __name__ == "__main__":
    print(get_git_commit_hash())
