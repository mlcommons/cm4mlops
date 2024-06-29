from cmind import utils
import os
import logging
def preprocess(i):
    os_info = i['os_info']

    env = i['env']
    script_path=i['run_script_input']['path']

    env["CM_SOURCE_FOLDER_PATH"] = script_path
    env['CM_C_SOURCE_FILES']="susan.c"

    if 'CM_INPUT' not in env:
        env['CM_INPUT'] = os.path.join(script_path, 'data.pgm')

    if 'CM_OUTPUT' not in env:
        env['CM_OUTPUT'] = 'output_image_with_corners.pgm'

    if 'CM_RUN_DIR' not in env:
        output_path = os.path.join(script_path, "output")
        if output_path!='' and not os.path.isdir(output_path):
            os.makedirs(output_path)

        env['CM_RUN_DIR'] = output_path

    env['CM_RUN_SUFFIX']= env['CM_INPUT'] + ' ' + env['CM_OUTPUT'] + ' -c'

    if os_info['platform'] == 'windows':
        env['CM_BIN_NAME']='image-corner.exe'
    else:
        env['CM_BIN_NAME']='image-corner'
        env['+ LDCFLAGS'] = ["-lm"]

    return {'return':0}

def postprocess(i):

    env = i['env']
    logging.info(env['CM_OUTPUT'] + " generated in " + env['CM_RUN_DIR'])

    return {'return':0}
