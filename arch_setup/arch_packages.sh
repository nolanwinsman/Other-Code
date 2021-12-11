#!/usr/bin/env bash
# To install a lot of packages I use
# Inspired by ArchTitus



echo '-----make sure snap is installed-----'

PKGS_PACMAN=(
'discord'
'telegram-desktop'
'networkmanager-openvpn'




)

PKGS_SNAP=(
'slack'
'qbittorrent-arnatious'


)

PKGS_PYTHON=(
'numpy'
)

# installs pacman packages
for PKG in "${PKGS_PACMAN[@]}"; do
    echo "INSTALLING: ${PKG}"
    sudo pacman -S "$PKG" --noconfirm --needed
done

# installs snap packages
for PKG in "${PKGS_SNAP[@]}"; do
    echo "INSTALLING: ${PKG}"
    sudo snap install "$PKG"
done

# installs python packages
for PKG in "${PKGS_PYTHON[@]}"; do
    echo "INSTALLING: ${PKG}"
    pip install "$PKG"
done

echo 'Things to setup'
echo 'Setup Surfshark'