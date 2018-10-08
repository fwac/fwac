#!/bin/bash
if ! ss -ant | grep 5050
then
  /usr/bin/pypi-server --disable-fallback -p 5050 /opt/python/packages &
fi
