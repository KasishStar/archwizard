import subprocess
import shutil
import os


def update_system():
    print("\nUpdating system...\n")

    result = subprocess.run([
        "sudo",
        "pacman",
        "-Syu"
    ])

    return result.returncode == 0


def bootstrap_aur_helper(helper_name):
    """
    Automatically installs base-devel, git, clones the requested AUR helper, 
    and builds/installs it cleanly via makepkg.
    """
    print(f"\n⚙️ Preparing system to install {helper_name}...")
    print("Installing build prerequisites (base-devel, git)...")
    
    # makepkg requires base-devel and git to compile software
    subprocess.run(["sudo", "pacman", "-S", "--needed", "--noconfirm", "base-devel", "git"])

    build_dir = f"/tmp/{helper_name}-build"
    
    # Clean up old build directories if they exist
    if os.path.exists(build_dir):
        subprocess.run(["rm", "-rf", build_dir])

    print(f"\n📂 Cloning {helper_name} from the AUR...")
    clone_res = subprocess.run(["git", "clone", f"https://aur.archlinux.org/{helper_name}.git", build_dir])

    if clone_res.returncode != 0:
        print(f"\n❌ Failed to clone {helper_name} repository.")
        return False

    print(f"\n🛠️ Building and installing {helper_name} via makepkg...")
    print("Note: You may be prompted for your sudo password to authorize the installation.")
    
    # makepkg MUST run as a normal user, not via sudo directly.
    # It will prompt the user for sudo access safely when installing the built package.
    build_res = subprocess.run(["makepkg", "-si", "--noconfirm"], cwd=build_dir)

    return build_res.returncode == 0


def install_packages(packages, method="pacman"):
    chosen_helper = None

    if method == "aur":
        # 1. Look for an existing helper automatically
        if shutil.which("yay"):
            chosen_helper = "yay"
        elif shutil.which("paru"):
            chosen_helper = "paru"
        else:
            # 2. No helper found! Time to guide non-tech-savvy users
            print("\n💡 What is an AUR Helper?")
            print("----------------------------------------------------------------------")
            print("You selected an AUR installation, but your system doesn't have an AUR helper.")
            print("The Arch User Repository (AUR) contains thousands of community packages.")
            print("To install them, you need a helper tool to download and compile them safely.")
            print("----------------------------------------------------------------------")
            print("\nWhich AUR Helper would you like ArchWizard to install for you?")
            print("1) yay  - Built in Go. The most popular, widely used, and beginner-friendly helper.")
            print("2) paru - Built in Rust. A modern, extremely fast alternative with advanced features.")
            print("3) Cancel - Fallback to standard pacman (Official packages only)")
            
            choice = input("\nSelect an option [1/2/3]: ")

            if choice == "1":
                if bootstrap_aur_helper("yay"):
                    chosen_helper = "yay"
            elif choice == "2":
                if bootstrap_aur_helper("paru"):
                    chosen_helper = "paru"
            
            # If bootstrapping failed or they canceled, fallback gracefully
            if not chosen_helper:
                print("\n⚠️ Falling back to official packages via standard pacman.")
                chosen_helper = "pacman"

    # 3. Formulate execution command based on helper status
    if chosen_helper in ["yay", "paru"]:
        cmd = [chosen_helper, "-S", "--needed"] + packages
        print(f"\n🚀 Installing packages via {chosen_helper}...")
    else:
        cmd = ["sudo", "pacman", "-S", "--needed"] + packages
        print("\n📦 Installing packages via pacman...")

    # 4. Execute final package installation command
    result = subprocess.run(cmd)

    if result.returncode == 0:
        print("\n✅ Installation successful!")
    else:
        print("\n❌ Installation failed!")

    input("\nPress Enter to continue...")

    return result.returncode == 0