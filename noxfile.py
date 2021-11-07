import nox

SOURCE_FILES = [
    "rfc6555.py",
    "tests/",
    "noxfile.py",
    "setup.py",
]


@nox.session()
def test(session):
    session.install("pytest", "pytest-cov")

    session.run("pytest", "--cov-config=.coveragerc", "tests/")


@nox.session()
def format(session):
    session.install("black", "isort")

    session.run("black", *SOURCE_FILES)
    session.run("isort", "--profile=black", *SOURCE_FILES)

    lint(session)


@nox.session
def lint(session):
    session.install("black", "isort", "flake8")

    session.run("black", "--check", *SOURCE_FILES)
    session.run("isort", "--check", "--profile=black", *SOURCE_FILES)
    session.run("flake8", "--ignore=E501", *SOURCE_FILES)
