#!/bin/bash
response=$(curl -s -w '%{size_download}' $1)
echo "$response"
