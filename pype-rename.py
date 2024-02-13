#!/usr/bin/env python

import sys, tempfile, os
import logging
from subprocess import check_call

EDITOR = os.environ.get('EDITOR', 'vim')
logger = logging.getLogger(__name__)

text = sys.stdin.read()
source_ = text.encode()

with tempfile.NamedTemporaryFile(suffix=".tmp") as tf: 
    tf.write(source_)
    old_names = source_.splitlines()
    tf.flush()

    stdin_fd = os.open('/dev/tty', os.O_RDONLY)
    os.dup2(stdin_fd, 0)
    os.close(stdin_fd)

    check_call([EDITOR, tf.name])

    new_names = open(tf.name).readlines()
    for i in range(len(new_names)):
        logger.debug("mv %s %s",
                     (old_names[i].decode(), new_names[i].rstrip()))
        os.rename(old_names[i].decode(), new_names[i].rstrip())
