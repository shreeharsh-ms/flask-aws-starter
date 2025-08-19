from setuptools import setup, find_packages

setup(
    name="flask-aws-app",
    version="0.1",
    packages=find_packages(include=["utils", "utils.*"]),
    install_requires=[
        "flask",
        "boto3"
    ],
    extras_require={
        "dev": ["pytest"]
    },
    entry_points={
        "console_scripts": [
            "flask-aws-app=app:app.run"
        ]
    },
    python_requires=">=3.7",
)
