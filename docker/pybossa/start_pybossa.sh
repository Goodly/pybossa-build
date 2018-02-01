#!/bin/bash
# somaxconn must be >= uwsgi listen setting.
if [[ -n ${PYBOSSA_SOMAXCONN} ]]; then
  sudo sysctl -w net.core.somaxconn=${PYBOSSA_SOMAXCONN}
else
  export PYBOSSA_SOMAXCONN=128 # Amazon Linux default
fi
exec /usr/local/bin/supervisord --nodaemon --configuration=/etc/supervisor/supervisord.conf
