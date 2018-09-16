yum install -y docker haproxy git
pip install pypiserver
pypi-server --disable-fallback -p 80 ~/packages &

