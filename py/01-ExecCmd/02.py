#! /usr/bin/python
#
#

#import sys
import subprocess
name="test"
proc = subprocess.Popen(['echo', name],
                            stdin = subprocess.PIPE,
                            stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE
                        )

(out, err) = proc.communicate()

print(out)


