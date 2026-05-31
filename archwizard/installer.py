import subprocess


def update_system():
    print("\nUpdating system...\n")

    result = subprocess.run([
        "sudo",
        "pacman",
        "-Syu"
    ])

    return result.returncode == 0


def install_packages(packages):
    cmd = ["sudo", "pacman", "-S", "--needed"] + packages

    result = subprocess.run(cmd)

    if result.returncode == 0:
        print("\n✅ Installation successful!")
    else:
        print("\n❌ Installation failed!")

    input("\nPress Enter to continue...")

    return result.returncode == 0