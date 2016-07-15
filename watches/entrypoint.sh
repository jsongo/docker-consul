#!/bin/bash
#!auth: jsongo

if [ -z "$WATCH_TYPE"  ]; then
    WATCH_TYPE=keyprefix
fi
if [ -z "$WATCH_TARGET"  ]; then
    WATCH_TARGET=/
fi
if [ -z "$SCRIPT"  ]; then
    SCRIPT=/script.sh
fi

if [ "$WATCH_TYPE" = "key" ]; then
    consul watch -type key -key $WATCH_TARGET $SCRIPT
elif [ "$WATCH_TYPE" = "keyprefix" ]; then
    consul watch -type keyprefix -prefix $WATCH_TARGET $SCRIPT
fi
