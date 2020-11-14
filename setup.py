from setuptools import setup

setup(
    name="tljh_docker_rights",
    author="namin",
    version="0.1",
    license="3-clause BSD",
    url='https://github.com/namin/tljh-docker-rights',
    entry_points={"tljh": ["docker_rights = tljh_docker_rights"]},
    py_modules=["tljh_docker_rights"],
)
