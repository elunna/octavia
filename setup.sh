#!/bin/bash
BINDIR=$HOME/bin
SCRIPT=octavia.py

ln --symbolic --verbose "$PWD/$SCRIPT" "$BINDIR/$SCRIPT"
