#!/bin/bash
# show top like stats for uwsgi processes and threads
source /home/pybossa/env/bin/activate
uwsgitop /tmp/pybossa-stats.sock
