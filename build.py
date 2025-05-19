import subprocess

def build():
    subprocess.run([
        "pyinstaller",
        "--onefile",
        "--name", "Epoch",
        "Epoch/__main__.py",
    ])

if __name__ == "__main__":
    build()
