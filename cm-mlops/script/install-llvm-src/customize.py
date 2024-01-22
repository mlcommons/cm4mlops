from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']

    clang_file_name = "clang"

    install_prefix = os.path.join(os.getcwd(), "install")
    if env.get('CM_LLVM_CONDA_ENV', '') == "yes":
        install_prefix = env['CM_CONDA_PREFIX']
        extra_cmake_options = f"-DCMAKE_SHARED_LINKER_FLAGS=-L{install_prefix} -Wl,-rpath,{install_prefix}"

    if env.get('CM_LLVM_16_INTEL_MLPERF_INFERENCE', '') == "yes":
        env['CM_REQUIRE_INSTALL'] = 'yes'
        i['run_script_input']['script_name'] = "install-llvm-16-intel-mlperf-inference"
        clang_file_name = "llvm-link"
        #env['USE_LLVM'] = install_prefix
        #env['LLVM_DIR'] = os.path.join(env['USE_LLVM'], "lib", "cmake", "llvm")
    else:
        if env.get('CM_LLVM_ENABLE_RUNTIMES', '') != '':
            enable_runtimes = env['CM_LLVM_ENABLE_RUNTIMES'].replace(":", ";")
        else:
            enable_runtimes = ''

        if env.get('CM_LLVM_ENABLE_PROJECTS', '') != '':
            enable_projects = env['CM_LLVM_ENABLE_PROJECTS'].replace(":", ";")
        else:
            enable_projects = ''

        llvm_build_type = env['CM_LLVM_BUILD_TYPE']

        cmake_cmd = "cmake " + os.path.join(env["CM_LLVM_SRC_REPO_PATH"], "llvm") + " -GNinja -DCMAKE_BUILD_TYPE="+llvm_build_type + " -DLLVM_ENABLE_PROJECTS="+ enable_projects+ " -DLLVM_ENABLE_RUNTIMES='"+enable_runtimes + "' -DCMAKE_INSTALL_PREFIX=" + install_prefix + " -DLLVM_ENABLE_RTTI=ON  -DLLVM_INSTALL_UTILS=ON -DLLVM_TARGETS_TO_BUILD=X86 " + extra_cmake_options

        env['CM_LLVM_CMAKE_CMD'] = cmake_cmd

    need_version = env.get('CM_VERSION','')

    #print(cmake_cmd)

    env['CM_LLVM_INSTALLED_PATH'] = install_prefix
    env['CM_LLVM_CLANG_BIN_WITH_PATH'] = os.path.join(env['CM_LLVM_INSTALLED_PATH'], "bin", clang_file_name)
    env['CM_GET_DEPENDENT_CACHED_PATH'] = env['CM_LLVM_CLANG_BIN_WITH_PATH']

    #env['+PATH'] = []
    return {'return':0}
