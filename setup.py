from setuptools import setup

requirements = []

setup(
    name="python-linting-test",
    description="Setting up a python package",
    author="Antonio Marco da Silva",
    author_email="antomarsi@hotmail.com",
    url="https://github.com/antomarsi/python-linting-test",
    install_requires=requirements,
    extras_require={
        "dev": [
            "bandit==1.7.0",
            "black==21.5b0",
            "flake8==3.9.1",
            "isort==5.8.0",
            "pre-commit==2.12.1",
        ]
    },
)
