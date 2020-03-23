import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='OSS Policy Sign',
     version='1.0',
     author="wyh",
     author_email="samuel.yh.wu@gmail.com",
     description="A django rest framework (DRF) policy sign for aliyun oss",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/wyh/oss-policy-sign",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: Apache License",
         "Operating System :: OS Independent",
     ],
 )
