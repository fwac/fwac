FROM centos:7

# Yum repo setup
RUN yum-config-manager --disable \*
COPY conf/FWAC-Base.repo /etc/yum.repos.d/FWAC-Base.repo
RUN yum -y install python-pip openssh-server openssh-clients && yum clean all

# sshd setup for ansible demo
RUN systemctl enable sshd.service;\
    yes y | ssh-keygen -f /root/.ssh/id_rsa -t rsa -N '';\
    cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys;\
    ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N '';\
    ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N '';\
    ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key -N ''  
COPY conf/ssh_config /root/.ssh/config

#pip config
COPY conf/.pip/pip.conf /root/.pip/pip.conf
RUN pip install --trusted-host pypi.local --upgrade pip

WORKDIR /opt/fwac/meeting02/labs

CMD ["/usr/sbin/sshd", "-D"]
