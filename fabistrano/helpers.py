import functools
from fabric.api import run, env


def dir_exists(dir):
    # return run('[ -d %s ] && echo 1 || echo 0' % dir) == '1'
    pass

def with_defaults(func):
    """A decorator that sets all defaults for a task."""

    @functools.wraps(func)
    def decorated(*args, **kwargs):
        env.setdefault('use_sudo', True)
        env.setdefault('git_branch', 'master')
        env.setdefault('python_bin', 'python')
        env.setdefault('remote_owner', 'www-data')
        env.setdefault('remote_group', 'www-data')


        env.setdefault('domain_path', "%(base_dir)s/%(app_name)s" % \
                                  { 'base_dir':env.base_dir,
                                    'app_name':env.app_name })
        env.setdefault('current_path', "%(domain_path)s/current" % \
                                       { 'domain_path':env.domain_path })
        env.setdefault('releases_path', "%(domain_path)s/releases" % \
                                        { 'domain_path':env.domain_path })
        env.setdefault('shared_path', "%(domain_path)s/shared" % \
                                      { 'domain_path':env.domain_path })
        if not env.has_key('releases'):
            if dir_exists(env.releases_path):
                env.releases = sorted(run('ls -x %(releases_path)s' % { 'releases_path':env.releases_path }).split())

                if len(env.releases) >= 1:
                    env.current_revision = env.releases[-1]
                    env.current_release = "%(releases_path)s/%(current_revision)s" % \
                                                { 'releases_path':env.releases_path, 
                                                  'current_revision':env.current_revision }
                if len(env.releases) > 1:
                    env.previous_revision = env.releases[-2]
                    env.previous_release = "%(releases_path)s/%(previous_revision)s" % \
                                                { 'releases_path':env.releases_path, 
                                                  'previous_revision':env.previous_revision }
        return func(*args, **kwargs)
    return decorated
