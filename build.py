import subprocess

def build():
    subprocess.run([
        "pyinstaller",
        "--onefile",
        "--name", "Epoch",
        "--icon", "Epoch/icon.png",
        "Epoch/__main__.py",
    ])

if __name__ == "__main__":
    build()