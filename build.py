import subprocess

def build():
    subprocess.run([
        "pyinstaller",
        "--onefile",
        "--name", "Epoch",
        "Epoch/__main__.py",
    ])
    subprocess.run([
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name", "Epoch-GUI",
        "--paths", ".",
        "Epoch/GUI.py"
    ])

if __name__ == "__main__":
    build()
