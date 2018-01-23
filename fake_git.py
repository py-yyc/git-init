import os
import subprocess

commit_metadata = {
    'name': 'Andrew',
    'email': 'andrew@example.org',
    'date': '1515151515 -0700' # time.strftime('%s %z')
}
git_env = {('GIT_%s_%s' % (who.upper(), what.upper()), value)
        for who in ['author', 'committer']
           for what, value in commit_metadata.items()}

def check_call(args):
    env = os.environ.copy()
    env.update(git_env)
    return subprocess.check_call(args, env=env)
