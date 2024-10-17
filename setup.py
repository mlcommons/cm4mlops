# setup.py
from setuptools import setup
from setuptools._distutils.dist import Distribution
from setuptools.command.install import install
import subprocess
import sys
import importlib.util
import platform
import os

# Try to use importlib.metadata for Python 3.8+ 
try:
    if sys.version_info >= (3, 8):
        from importlib.metadata import version, PackageNotFoundError
    else:
        # Fallback to pkg_resources for Python < 3.8
        import pkg_resources
        PackageNotFoundError = pkg_resources.DistributionNotFound
except ImportError:
    # If importlib.metadata is unavailable, fall back to pkg_resources
    import pkg_resources
    PackageNotFoundError = pkg_resources.DistributionNotFound



class CustomInstallCommand(install):
    def run(self):
        self.get_sys_platform()
        self.install_system_packages()

        # Call the standard run method
        install.run(self)

        # Call the custom function
        return self.custom_function()

    def is_package_installed(self, package_name):
        try:
            if sys.version_info >= (3, 8):
                version(package_name)  # Tries to get the version of the package
            else:
                pkg_resources.get_distribution(package_name)  # Fallback for < 3.8
            return True
        except PackageNotFoundError:
            return False

    def install_system_packages(self):
        # List of packages to install via system package manager
        packages = []
        
        git_status = self.command_exists('git')
        if not git_status:
            packages.append("git")
        wget_status = self.command_exists('wget')
        if not wget_status:
            packages.append("wget")
        curl_status = self.command_exists('curl')
        if not curl_status:
            packages.append("curl")

        name='venv'

        if name in sys.modules:
            pass #nothing needed
        elif self.is_package_installed(name):
            pass
        else:
            packages.append("python3-venv")
        
        if packages:
            if self.system == 'Linux' or self.system == 'Darwin':
                manager, details = self.get_package_manager_details()
                if manager:
                    if manager == "apt-get":
                        subprocess.check_call(['sudo', 'apt-get', 'update'])
                        subprocess.check_call(['sudo', 'apt-get', 'install', '-y'] + packages)
            elif self.system == 'Windows':
                print(f"Please install the following packages manually: {packages}")



    def detect_package_manager(self):
        package_managers = {
            'apt-get': '/usr/bin/apt-get',
            'yum': '/usr/bin/yum',
            'dnf': '/usr/bin/dnf',
            'pacman': '/usr/bin/pacman',
            'zypper': '/usr/bin/zypper',
            'brew': '/usr/local/bin/brew'
        }

        for name, path in package_managers.items():
            if os.path.exists(path):
                return name

        return None

    def get_package_manager_details(self):
        manager = self.detect_package_manager()
        if manager:
            try:
                version_output = subprocess.check_output([manager, '--version'], stderr=subprocess.STDOUT).decode('utf-8')
                return manager, version_output.split('\n')[0]
            except subprocess.CalledProcessError:
                return manager, 'Version information not available'
        else:
            return None, 'No supported package manager found'

    # Checks if command exists(for installing required packages).
    # If the command exists, which returns 0, making the function return True.
    # If the command does not exist, which returns a non-zero value, making the function return False.
    # NOTE: The standard output and standard error streams are redirected to PIPES so that it could be captured in future if needed.    
    def command_exists(self, command):
        if self.system == "Linux" or self.system == 'Darwin':
            return subprocess.call(['which', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0
        elif self.system == "Windows":
            return subprocess.call([command, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) == 0

    def custom_function(self):
        import cmind
        #r = cmind.access({'action':'rm', 'automation':'repo', 'data_uoa':'mlcommons@cm4mlops', 'force': True})
        r = cmind.access({'action':'pull', 'automation':'repo', 'artifact':'mlcommons@cm4mlops', 'branch': 'mlperf-inference'})
        print(r)
        if r['return'] > 0:
           return r['return']
    
    def get_sys_platform(self):
        self.system =  platform.system() 

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='cm4mlops',
    version='0.3',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/mlcommons/cm4mlops",
    packages=[],
    install_requires=[
        "setuptools>=60",
        "wheel",
        "cmind",
        "giturlparse",
        "requests",
        "pyyaml"
        ],
    cmdclass={
        'install': CustomInstallCommand,
    },
)
