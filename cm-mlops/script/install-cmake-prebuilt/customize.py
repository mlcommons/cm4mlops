from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    automation = i['automation']

    recursion_spaces = i['recursion_spaces']

    need_version = env.get('CM_VERSION','')
    if need_version == '':
        return {'return':1, 'error':'internal problem - CM_VERSION is not defined in env'}

    print (recursion_spaces + '    # Requested version: {}'.format(need_version))

    host_os_bits = env['CM_HOST_OS_BITS']

    if os_info['platform'] != 'windows':
        host_os_machine = env['CM_HOST_OS_MACHINE'] # ABI

    # Prepare package name
    if os_info['platform'] == 'darwin':
        if host_os_bits != '64':
            return {'return':1, 'error':'this package doesn\'t support non 64-bit MacOS'}

        package_name = 'cmake-' + need_version + '-macos-universal.tar.gz'

    elif os_info['platform'] == 'windows':
        package_name = 'cmake-' + need_version + '-windows-'

        if host_os_bits == '64':
            package_name += 'x86_64'
        else:
            package_name += 'i386'

        package_name += '.zip'

    else:
       package_name='cmake-' + need_version + '-linux-'

       if host_os_machine.startswith('arm') or host_os_machine.startswith('aarch'):
          if host_os_bits=='64':
              package_name += 'aarch64'
          else:
              return {'return':1, 'error':'this script doesn\'t support armv7'}
       else:
          package_name += 'x86_64'

       package_name +=  '.tar.gz'


    package_url = 'https://github.com/Kitware/CMake/releases/download/v' + need_version + '/' + package_name

    print (recursion_spaces + '    # Prepared package URL: {}'.format(package_url))

    print ('')
    print ('Downloading from {} ...'.format(package_url))

    cm = automation.cmind

    r = cm.access({'action':'download_file', 
                   'automation':'utils,dc2743f8450541e3', 
                   'url':package_url})
    if r['return']>0: return r

    filename = r['filename']

    # Check what to do with this file depending on OS
    if os_info['platform'] == 'windows':
        print ('Unzipping file {}'.format(filename))

        r = cm.access({'action':'unzip_file', 
                       'automation':'utils,dc2743f8450541e3', 
                       'strip_folders':1,
                       'filename':filename})
        if r['return']>0: return r

        if os.path.isfile(filename):
            print ('Removing file {}'.format(filename))
            os.remove(filename)

        path_bin = os.path.join(os.getcwd(), 'bin')
    elif os_info['platform'] == 'darwin':
        path_bin = os.path.join(os.getcwd(), 'CMake.app', 'Contents', 'bin')
    else:
        path_bin = os.path.join(os.getcwd(), 'bin')

    env['CM_CMAKE_PACKAGE'] = filename

    # Needed to finalize detection of this package
    # via another script and do not search again
    env['CM_TMP_PATH'] = path_bin
    env['CM_TMP_FAIL_IF_NOT_FOUND'] = 'yes'

    return {'return':0}
