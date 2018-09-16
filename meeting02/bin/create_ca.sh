#!/bin/bash
mkdir /opt/ca 2>/dev/null
DIR=`pwd`
cd /opt/ca
openssl genrsa -des3 -out myCA.key 2048
openssl req -x509 -new -nodes -key myCA.key -sha256 -days 3650 -out myCA.pem
cp myCA.pem $DIR
cd -
