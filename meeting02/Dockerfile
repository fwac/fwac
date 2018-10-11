FROM centos:7

RUN yum-config-manager --disable \*
#RUN yum -y install epel-release && yum clean all

COPY conf/FWAC-Base.repo /etc/yum.repos.d/FWAC-Base.repo
RUN yum -y install python-pip openssh-server openssh-clients && yum clean all
RUN chkconfig sshd on; yes y | ssh-keygen -f /root/.ssh/id_rsa -t rsa -N '';cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys
RUN pip install --upgrade pip;mkdir -p /root/.pip

COPY conf/pip.conf /root/.pip/pip.conf

WORKDIR /opt/fwac/meeting02/labs

CMD while true; do sleep 10; done
