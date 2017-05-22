#!/bin/bash
set -e
cd /home/pybossa/repo
. /home/pybossa/env/bin/activate
# db_create adds two default categories and doesn't reset DB
# python cli.py db_create
# Reset DB from scratch
python cli.py db_rebuild
