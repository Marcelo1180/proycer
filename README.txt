//INSTALACION DE PUPPETMASTER
wget http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
rpm -ivh epel-release-6-8.noarch.rpm

yum -y install http://yum.theforeman.org/releases/1.5/el6/x86_64/foreman-release.rpm
yum -y install foreman-installer

vi /etc/hosts
127.0.0.1 foreman.localhost.foreman foreman

vi /etc/hostname
foreman

hostname foreman.localhost.foreman

foreman-installer


























yum install gcc make python-devel
yum -y install python-pip --enablerepo epel
pip install virtualenvwrapper
pip install -r requirements.txt
pip install django-location-field
pip install gunicorn setproctitle

//INSTALACION DE POSTGRES
sudo yum localinstall http://yum.postgresql.org/9.3/redhat/rhel-6-x86_64/pgdg-centos93-9.3-1.noarch.rpm
sudo yum install postgresql postgresql-devel postgresql-server python-psycopg2 proj-epsg proj-nad postgis
sudo service postgresql initdb
sudo service postgresql start
sudo chkconfig postgresql on
sudo passwd postgres
:Snake1180
su postgres
psql
ALTER ROLE postgres WITH PASSWORD 'Snake1180';
CREATE USER xu_sisget WITH PASSWORD 'Ker101180dgtic';
CREATE DATABASE sisget_db;
GRANT ALL PRIVILEGES ON DATABASE sisget_db to xu_sisget;
\q
psql -U postgres -d sisget_db -f /home/www/django_maps/dumpfilename.sql
exit
#cambiar a md5 la autenticacion
vi /var/lib/pgsql/data/pg_hba.conf
service postgresql restart

//INICIANDO NGINX
yum install nginx
chkconfig nginx on
service nginx start

//INICIANDO SUPERVISOR
pip install supervisor
echo_supervisord_conf > /etc/supervisord.conf
mkdir /var/log/supervisor
vim /etc/supervisord.conf
# Modifique las siguientes configuraciones
[unix_http_server] 
...
file=/var/run/supervisor.sock
...
[supervisord]
...
logfile=/var/log/supervisor/supervisord.log
pidfile=/var/run/supervisord.pid 
umask=022
user=root
...

vim /etc/init.d/supervisord
#!/bin/bash
#
# supervisord   This scripts turns supervisord on
#
# chkconfig: - 95 04
#
# processname:  supervisord
# config: /etc/supervisord.conf
#
 
# source function library
. /etc/rc.d/init.d/functions
 
RETVAL=0
conffile=${CONFFILE-/etc/supervisord.conf}
user=${USER-root}
 
start() {
        echo -n $"Starting supervisord: "
        runuser -l ${user} -c "supervisord -c ${conffile}" && echo_success || echo_failure
        RETVAL=$?
        echo
        [ $RETVAL -eq 0 ] && touch /var/lock/subsys/supervisord
}
 
stop() {
 echo -n $"Stopping supervisord: "
 killproc supervisord
 echo
 [ $RETVAL -eq 0 ] && rm -f /var/lock/subsys/supervisord
}
 
restart() {
 stop
 start
}
 
case "$1" in
  start)
 start
 ;;
  stop) 
 stop
 ;;
  restart|force-reload|reload)
 restart
 ;;
  condrestart)
 [ -f /var/lock/subsys/supervisord ] && restart
 ;;
  status)
 status supervisord
 RETVAL=$?
 ;;
  *)
 echo $"Usage: $0 {start|stop|status|restart|reload|force-reload|condrestart}"
 exit 1
esac
 
exit $RETVAL


chkconfig --add supervisord
chkconfig supervisord on
chmod 777 /etc/init.d/supervisord
service supervisord start
vi /etc/supervisord.conf
# Agregue este bloque de configuracion segun su proyecto
[program:django_maps]
command=/opt/gunicorn/django_maps/gunicorn_start.sh
user=root
autostart=true
autorestart=true
stdout_logfile=/var/log/supervisor/django_maps.log
redirect_stderr=True


//INICIANDO GUNICORN
gunicorn django_maps.wsgi
mkdir -p /opt/gunicorn/django_maps/
vi /opt/gunicorn/django_maps/gunicorn_start.sh

!/bin/bash

DJANGODIR=/home/www/django_maps             # Directorio del proyecto Django
SOCKFILE=/var/run/gunicorn/django_maps.sock # Unix socket
USER=nginx                                    # Usuario
GROUP=root                                    # Grupo
NUM_WORKERS=3                                 # Numero de procesos para gunicorn
DJANGO_SETTINGS_MODULE=django_maps.settings # Archivo settings del proyecto
DJANGO_WSGI_MODULE=django_maps.wsgi         # Modulo WSGI del proyecto

# Activar el entorno virtual
cd $DJANGODIR
#source /usr/bin/virtualenvwrapper.sh
#workon django_maps
#export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
#export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Crear el directorio del socket si no existe
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Iniciar el proyecto Django
# No se usa el modo --daemon ya que este sera manejado por supervisor
exec gunicorn ${DJANGO_WSGI_MODULE} \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --log-level=debug \
#  --bind=unix:$SOCKFILE

chmod u+x /opt/gunicorn/django_maps/gunicorn_start.sh
sh /opt/gunicorn/django_maps/gunicorn_start.sh

//Configurando NGINX
vi /et/nginx/nginx.conf
#agregar la siguiente linea de inclusiom
include /etc/nginx/sites-enabled/*;

mkdir /etc/nginx/sites-enabled
vi /etc/nginx/sites-enabled/django-maps
server {
    listen *:8001;

    location /static  {
        alias /home/www/django_maps/static;
    }

    location / {
        proxy_pass_header Server;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Scheme $scheme;
        proxy_connect_timeout 10;
        proxy_read_timeout 100;
        proxy_pass http://127.0.0.1:8000/;
    }
}
service nginx restart
iptables -I INPUT -p tcp --dport 8001 -j ACCEPT
service iptables save
service iptables restart