import os
import subprocess
import time
from copy import copy

import requests

from homework7 import settings

repo_root = os.path.abspath(os.path.join(__file__, os.pardir))


def wait_ready(host, port):
    # Ожидание того, что приложение запущено
    start = False
    st = time.time()
    while time.time() - st <= 5:
        try:
            requests.get(f'http://{host}:{port}')
            start = True
            break
        except ConnectionError:
            pass
    if not start:
        raise RuntimeError('App did not started in 3s!')


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        #### app configuration ####
        app_path = os.path.join(repo_root, 'application', 'app.py')
        env = copy(os.environ)
        env.update({'APP_HOST': settings.APP_HOST, 'APP_PORT': settings.APP_PORT})
        # Логи
        app_stderr_path = os.path.join(repo_root, 'logs', 'app_stderr')
        app_stdout_path = os.path.join(repo_root, 'logs', 'app_stdout')
        app_stderr = open(app_stderr_path, 'w')
        app_stdout = open(app_stdout_path, 'w')
        app_proc = subprocess.Popen(
            ['C:\\Users\\Olyan\\Desktop\\homework_vk_education\\venv\\Scripts\\python.exe', app_path],
            stderr=app_stderr, stdout=app_stdout)
        # Сохраняем параметры для дальнейшего их закрытия
        config.app_stderr = app_stderr
        config.app_stdout = app_stdout
        config.app_proc = app_proc
        wait_ready(settings.APP_HOST, settings.APP_PORT)

        #### stub configuration ####
        stub_path = os.path.join(repo_root, 'stub', 'flask_stub.py')
        env = copy(os.environ)
        env.update({'STUB_HOST': settings.STUB_HOST, 'STUB_PORT': settings.STUB_PORT})  # TODO ПОнять для чего
        # Логи
        stub_stderr_path = os.path.join(repo_root, 'logs', 'app_stderr')
        stub_stdout_path = os.path.join(repo_root, 'logs', 'app_stdout')
        stub_stderr = open(stub_stderr_path, 'w')
        stub_stdout = open(stub_stdout_path, 'w')
        stub_proc = subprocess.Popen(
            ['C:\\Users\\Olyan\\Desktop\\homework_vk_education\\venv\\Scripts\\python.exe', stub_path],
            stderr=stub_stderr, stdout=stub_stdout)
        # Сохраняем параметры для дальнейшего их закрытия
        config.stub_stderr = stub_stderr
        config.stub_stdout = stub_stdout
        config.stub_proc = stub_proc
        wait_ready(settings.STUB_HOST, settings.STUB_PORT)


def pytest_unconfigure(config):
    # Закрытие процесса
    config.app_proc.terminate()
    exit_code = config.app_proc.wait()

    # Закрытие дескрипторов
    config.app_stderr.close()
    config.app_stdout.close()
    assert exit_code == 1

    # Закрытие процесса
    config.stub_proc.terminate()
    exit_code = config.stub_proc.wait()

    # Закрытие дескрипторов
    config.stub_stderr.close()
    config.stub_stdout.close()
    assert exit_code == 1
