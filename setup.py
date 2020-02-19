from setuptools import setup, find_packages

setup(
    name='predict_functions_package',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A list of python Data Analysis Functions',
    long_description=open('README.md').read(),
    install_requires=['numpy', 'pandas'],
    url='https://github.com/bmsimang/Analyse_Function_Predict',
    author='Bongani Msimanga, Azukile Kobe, Vinita Maharaj, Shraddha Rajcoomar, Akshar Jadoonandan',
    author_email='bonganimsimanga0@gmail.com, dhrtirajcoomar@gmail.com, azukilekobe11@gmail.com, vinita.maharaj@gmail.com, aksharj003@gmail.com'
)