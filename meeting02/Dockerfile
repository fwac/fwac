FROM centos:7

RUN yum -y install epel-release && yum clean all
RUN yum -y install python-pip && yum clean all
RUN pip install --upgrade pip;mkdir -p /root/.pip

COPY conf/pip.conf /root/.pip/pip.conf
COPY myCA.pem /root/myCA.pem

WORKDIR /opt/fwac

CMD while true; do sleep 10; done
