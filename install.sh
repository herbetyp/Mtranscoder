#!/usr/bin/env bash

# mtranscoder installation script

# creates director Mtranscoder at / opt
sudo mkdir /opt/Mtranscoder

# Copy the files for folder /opt
sudo cp -r libs /opt/Mtranscoder && sudo cp mtranscoder /opt/Mtranscoder

# Create symbolic mtranscoder link to /usr/local/bin
sudo ln -s /opt/Mtranscoder/mtranscoder /usr/local/bin

# Create symbolic libs link to /usr/local/bin
sudo ln -s /opt/Mtranscoder/libs /usr/local/bin
