#!/bin/bash
IP=`hostname -i`
NAME=$1
if ! test $TAG
then
  echo "TAG environment variable not set!"
  exit 1
fi
if test $NAME
then
  echo
  if docker run -d -it -v /opt/fwac:/opt/fwac -e NAME=$NAME --hostname $NAME --dns=10.0.0.1 --add-host="fwac:$IP" --add-host="pypi.local:$IP" --name=$NAME $TAG &> /tmp/$NAME
  then
    echo "Created new container named $NAME"
  elif docker start $NAME &>> /tmp/$NAME
  then
    echo "Using existing container $NAME"
  else
    echo "Assuming $NAME is already running"
  fi
  sleep 2
  echo
  if ! docker exec -it $NAME bash -c 'mkdir $HOSTNAME 2>/dev/null; cd $HOSTNAME; exec "${SHELL:-sh}"'
  then
    echo "I didn't make it into the container :("
    echo "You're on your own now"
  fi
  echo
else
  echo "$0 container_name"
fi
