from fabric.api import *

env.short_name = 'freelance_django'
env.venv_path = '/root/.virtualenvs/'
env.venv = 'source %s%s/bin/activate' % (env.venv_path, env.short_name)
env.base_dir = '/usr/src/'
env.domain = 'ryanjurgensen.com'
env.dir = '/usr/src/%s' % (env.short_name)
env.git = 'git@github.com:ryanjurgensen/freelance_django.git'
env.hosts = ['ec2-50-112-37-104.us-west-2.compute.amazonaws.com ']
env.user = 'ubuntu'
env.deploy_user = 'root'

upstart_file = """
env NEW_RELIC_CONFIG_FILE=%s/newrelic.ini
exec newrelic-admin run-program uwsgi \
--uid=root \
--home=/root/.virtualenvs/freelance_django \
--pythonpath=/usr/src/freelance_django \
--chdir=/usr/src/freelance_django \
--socket=/tmp/uwsgi.sock \
--module=freelance_django.wsgi:application \
--env DJANGO_SETTINGS_MODULE=freelance_django.settings \
--chmod-socket \
--logdate \
--optimize 2 \
--processes 6 \
--master \
--harakiri=60 \
--vacuum \
--logto /var/log/freelance_django-uwsgi.log \
--buffer-size=8196 \
--enable-threads \
--single-interpreter
"""

nginx_file = """upstream django {
    server unix:///tmp/uwsgi.sock;
    #server 127.0.0.1:8001;
}
server {
    listen 80;
    server_name %s;
    access_log /var/log/%s.log;
    error_log /var/log/%s.error.log;

    location /static/ { # STATIC_URL
        alias %s/freelance_django/static_root/; # STATIC_ROOT
        expires 30d;
    }

    location /media/ { # MEDIA_URL
        alias %s/freelance_django/static_root/media/; # MEDIA_ROOT
        expires 30d;
    }

    location / {
        include uwsgi_params;
        uwsgi_pass django;
    }
}
""" % (env.domain, env.short_name, env.short_name, env.dir, env.dir)
def venv(command):
    with cd(env.dir):
        sudo(env.venv + ' && ' + command, user=env.deploy_user)

def install_prereqs():
    sudo('apt-get install nginx python-setuptools git gcc python-dev upstart python-flup libmysqlclient-dev memcached')
    sudo('easy_install virtualenv')
    sudo('pip install newrelic')

def setup_virtualenv():
	sudo('mkdir -p ' + env.venv_path, user=env.deploy_user)
	with cd(env.venv_path):
		sudo('virtualenv --no-site-packages %s' % env.short_name)

def get_project():
	with cd(env.base_dir):
		sudo('rm -rf %s' % env.short_name)
		sudo('git clone %s' % env.git)

def install_newrelic():
    print 'Installing newrelic'
    with cd(env.dir):
        venv('newrelic-admin generate-config b57fa342a913717b243fc04ba7044dd49d86ba04 newrelic.ini')
        sudo('NEW_RELIC_CONFIG_FILE=%s/newrelic.ini' % env.dir)
        sudo('export NEW_RELIC_CONFIG_FILE')

def setup_servers():
    venv('pip install uwsgi')
    upstart = upstart_file % (env.dir)
    sudo('echo "%s" > /etc/init/%s.conf' % (upstart, env.short_name), user=env.deploy_user)

    sudo('echo "%s" > /etc/nginx/sites-available/%s.conf' % (nginx_file, env.short_name), user=env.deploy_user)
    sudo('ln -sf /etc/nginx/sites-available/%s.conf /etc/nginx/sites-enabled/%s.conf' % (env.short_name, env.short_name))
    sudo('service nginx restart')
    with cd(env.dir):
        sudo('ln -sf ./configs/prod.py ./local_settings.py')
        venv('pip install -r requirements.txt')
        install_newrelic()
    sudo('restart %s' % env.short_name)

def genesis():
    install_prereqs()
    setup_virtualenv()
    get_project()
    setup_servers()

def restart():
    print 'Restarting uWSGI'
    with settings(hide('warnings', 'running', 'stdout', 'stderr')):
        sudo('restart dynamo')

def deploy(tag='master'):
    env.hosts_complete = 0
    print '***** DEPLOYING *****'

    with settings(hide('warnings', 'running', 'stdout', 'stderr')):
        with cd(env.dir):
            # check out code
            print 'Updating source code'
            sudo('git checkout master && git pull && git checkout %s && git pull origin %s' % (tag, tag))

            revision = sudo('git rev-parse HEAD')
            print 'Current revision is: %s' % revision

            # install dependencies
            print 'Installing dependencies'
            venv('pip install -r requirements.txt')
            venv('python manage.py collectstatic --noinput')
            if env.hosts_complete < 1: # Only perform these tasks once.
                # django stuff
                print 'Running syncdb'
                venv('python manage.py syncdb')
                with settings(warn_only=True):
                    print 'Running migrate'
                    venv('python manage.py migrate')

    restart()
    env.hosts_complete += 1
	