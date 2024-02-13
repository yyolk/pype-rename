#!/usr/bin/env python
import os
import logging
import sys
import tempfile

from subprocess import check_call


EDITOR = os.environ.get("EDITOR", "vim")

logger = logging.getLogger(__name__)

text = sys.stdin.read()
source_ = text.encode()
# Assume every line is a different filename
old_names = source_.splitlines()

with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
    tf.write(source_)
    tf.flush()

    stdin_fd = os.open("/dev/tty", os.O_RDONLY)
    os.dup2(stdin_fd, 0)
    os.close(stdin_fd)

    # Ensure the editor is closed
    check_call([EDITOR, tf.name])

    new_names = open(tf.name).readlines()

for i in range(len(new_names)):
    logger.debug("mv %s %s", (old_names[i].decode(), new_names[i].rstrip()))
    # Direct line index mapping of input to output.
    os.rename(old_names[i].decode(), new_names[i].rstrip())
