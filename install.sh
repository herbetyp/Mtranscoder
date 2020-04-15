#!/usr/bin/env bash

# mtranscoder installation script

# creates director Mtranscoder at / opt
sudo mkdir -p /opt/Mtranscoder

# Copy the files for folder /opt
sudo cp -r libs /opt/Mtranscoder && sudo cp mtranscoder /opt/Mtranscoder

# Create symbolic mtranscoder link to /usr/local/bin
sudo rm -f /usr/local/bin/mtranscoder
sudo ln -s /opt/Mtranscoder/mtranscoder /usr/local/bin/mtranscoder
