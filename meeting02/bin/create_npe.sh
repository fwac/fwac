if test $1
then
  cd /opt/ca
  openssl genrsa -out ${1}.key 2048
  openssl req -new -key ${1}.key -out ${1}.csr
  openssl x509 -req -in ${1}.csr -CA myCA.pem -CAkey myCA.key -CAcreateserial -out ${1}.crt -days 1825 -sha256 -extfile pypi.local.ext
  cd -
else
  echo "pass name or fqdn"
fi
