#!/bin/bash
# curl a websites size
echo "$(curl -s -w '%{size_download}' $1)"
