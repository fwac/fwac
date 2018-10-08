FROM centos:7

RUN yum-config-manager --disable \*
#RUN yum -y install epel-release && yum clean all

COPY conf/FWAC-Base.repo /etc/yum.repos.d/FWAC-Base.repo
RUN yum -y install python-pip && yum clean all
RUN pip install --upgrade pip;mkdir -p /root/.pip

COPY conf/pip.conf /root/.pip/pip.conf

WORKDIR /opt/fwac

CMD while true; do sleep 10; done
