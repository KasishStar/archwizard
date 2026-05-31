# ArchWizard

A community-driven setup wizard for Arch Linux.

ArchWizard helps users quickly install common software profiles after a fresh Arch Linux installation. Instead of manually installing the same packages every time, users can choose a profile and let ArchWizard handle the setup.

## Features

* Gaming setup profile
* Developer setup profile
* Hyprland setup profile
* Beginner-friendly terminal interface
* Uses native Arch Linux package management
* Lightweight and fast

## Installation

Clone the repository:

```bash
git clone git@github.com:KasishStar/archwizard.git
cd archwizard
```

Run:

```bash
python archwizard/main.py
```

## Profiles

### Gaming

* Steam
* Lutris
* Discord
* MangoHud
* Gamemode

### Developer

* Git
* Python
* NodeJS
* Docker

### Hyprland

* Hyprland
* Waybar
* Kitty
* Rofi
* Swaybg

## Security

ArchWizard uses `sudo pacman` to update the system and install selected packages.

Your password is requested by `sudo` and is handled by the operating system. ArchWizard does not collect, store, transmit, log, or upload passwords.

## Community

Discord server:

Replace this line with your Discord invite link.

Community feedback, bug reports, feature requests, and discussions are welcome.

## Roadmap

### Version 1

* Package installation profiles
* Basic terminal interface

### Version 2

* Student profile
* Content creator profile
* Minimal setup profile

### Version 3

* AUR support
* Automatic yay/paru detection

### Version 4

* Profile export/import

## Contributing

Pull requests, bug reports, and suggestions are welcome.

## License

MIT License
