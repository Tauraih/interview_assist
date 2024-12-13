import os
from pathlib import Path
import sys

import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent
IS_TEST = 'test' in sys.argv or 'test_coverage' in sys.argv


def load_envronment():
    env = environ.Env()
    if env.str('SECRET_KEY', default='') == '':
        env_file = env.str('ENV', default=None)
        if env_file:
            if not env_file.endswith('.env'):
                env_file += '.env'
            env_file = os.path.join(BASE_DIR.parent, 'environments', env_file)
        else:
            env_file = os.path.join(BASE_DIR.parent, '.env')
        print(f'Loading environment from: {env_file}')
        env.read_env(env_file)
    return env


env = load_envronment()