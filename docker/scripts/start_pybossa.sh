#!/bin/bash
# somaxconn must be >= uwsgi listen setting.
if [[ -n ${PYBOSSA_SOMAXCONN} ]]; then
  echo "Attempting to set SOMAXCONN to: ${PYBOSSA_SOMAXCONN}"
  sudo sysctl -w net.core.somaxconn=${PYBOSSA_SOMAXCONN}
fi
export PYBOSSA_SOMAXCONN=$(sysctl -n net.core.somaxconn)
echo "Log tuning parameters used by uWSGI and NGINX:"
echo "SOMAXCONN - maximum TCP/IP queue backlog: ${PYBOSSA_SOMAXCONN}"
echo "Max open file descriptors: hard limit $(ulimit -Hn) soft limit $(ulimit -Sn)"
exec /usr/local/bin/supervisord --nodaemon --configuration=/etc/supervisor/supervisord.conf
