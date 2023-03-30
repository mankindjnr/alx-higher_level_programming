#!/bin/bash
# curl a websites size
curl -s -w '%{size_download}\n' "$1"
