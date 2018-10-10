#!/bin/bash
if ! ss -ant | grep 5050
then
  /usr/bin/pypi-server --disable-fallback -i 127.0.0.1 -p 5050 -v --log-file /var/log/pypi.log /opt/python/packages &
fi
