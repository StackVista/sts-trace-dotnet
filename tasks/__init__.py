"""
Invoke entrypoint, import here all the tasks we want to make available
"""
import os
import invoke
from invoke import Collection
from invoke import task
from invoke.exceptions import Exit

from .utils    import get_version
from .branding import apply_branding

@task
def version(ctx, url_safe=False, git_sha_length=8):
    """
    Get the agent version.
    url_safe: get the version that is able to be addressed as a url
    git_sha_length: different versions of git have a different short sha length,
                    use this to explicitly set the version
                    (the windows builder and the default ubuntu version have such an incompatibility)
    """
    print(get_version(ctx, include_git=True, url_safe=url_safe, git_sha_length=git_sha_length))

# the root namespace
ns = Collection()

# add single tasks to the root
ns.add_task(version)
ns.add_task(apply_branding)

ns.configure({
    'run': {
        # workaround waiting for a fix being merged on Invoke,
        # see https://github.com/pyinvoke/invoke/pull/407
        'shell': os.environ.get('COMSPEC', os.environ.get('SHELL')),
        # this should stay, set the encoding explicitly so invoke doesn't
        # freak out if a command outputs unicode chars.
        'encoding': 'utf-8',
    }
})
