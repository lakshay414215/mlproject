from setuptools import find_packages,setup


def get_requirements(filepath:str)->list[str]:
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]


        if "-e ." in requirements:
            requirements.remove("-e .")


    return requirements

setup (
name="machinelearningproject",
version="0.0.1",
author="Lakshay",
author_email="lakshaysain2611@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')



)