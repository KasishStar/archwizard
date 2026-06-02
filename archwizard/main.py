from .profiles import PROFILES
from .installer import install_packages, update_system


def show_menu():
    print("""
╔══════════════════════╗
║      ARCHWIZARD      ║
╚══════════════════════╝

1. Gaming Setup
2. Developer Setup
3. Hyprland Setup
4. Exit
""")


def main():
    while True:
        show_menu()

        choice = input("Select option: ")

        if choice == "1":
            profile = "gaming"

        elif choice == "2":
            profile = "developer"

        elif choice == "3":
            profile = "hyprland"

        elif choice == "4":
            break

        else:
            print("\nInvalid option.")
            continue

        update = input(
            "\nA system update is recommended before installing packages.\nUpdate now? (Y/n): "
        )

        if update.lower() != "n":
            success = update_system()

            if not success:
                print("\n❌ System update failed.")
                input("\nPress Enter to continue...")
                continue

        packages = PROFILES[profile]

        print("\nPackages to install:\n")

        for pkg in packages:
            print("-", pkg)

        confirm = input("\nContinue? (Y/n): ")

        if confirm.lower() != "n":
            # Prompt for Pacman vs AUR
            print("\nSelect Installation Method:")
            print("1. Standard (pacman)")
            print("2. AUR Helper (yay/paru)")
            method_choice = input("Select option [1/2]: ")

            method = "aur" if method_choice == "2" else "pacman"

            install_packages(packages, method=method)


if __name__ == "__main__":
    main()