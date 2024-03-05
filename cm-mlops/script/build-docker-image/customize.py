from cmind import utils
import os
from os.path import exists

def preprocess(i):

    os_info = i['os_info']
    env = i['env']

    dockerfile_dir = env.get('CM_DOCKERFILE_WITH_PATH')
    if dockerfile_dir and os.path.exists(dockerfile_dir):
        os.chdir(os.path.dirname(dockerfile_dir))

    CM_DOCKER_BUILD_ARGS = env.get('+ CM_DOCKER_BUILD_ARGS', [])

    if 'CM_GH_TOKEN' in env:
        CM_DOCKER_BUILD_ARGS.append( "CM_GH_TOKEN="+env['CM_GH_TOKEN'] )

    if CM_DOCKER_BUILD_ARGS:
        build_args = "--build-arg "+ " --build-arg ".join(CM_DOCKER_BUILD_ARGS)
    else:
        build_args = ""

    env['CM_DOCKER_BUILD_ARGS'] = build_args

    if 'CM_DOCKERFILE_WITH_PATH' not in env or not exists(env['CM_DOCKERFILE_WITH_PATH']):
        env['CM_BUILD_DOCKERFILE'] = "yes"
    else:
        env['CM_BUILD_DOCKERFILE'] = "no"

    if "CM_DOCKER_IMAGE_REPO" not in env:
        env['CM_DOCKER_IMAGE_REPO'] = "local"

    docker_image_name = env.get('CM_DOCKER_IMAGE_NAME', '')
    if docker_image_name == '':
        docker_image_name = env.get('CM_DOCKER_RUN_SCRIPT_TAGS','').replace(',', '-').replace('_','')
    if docker_image_name == '':
        docker_image_name = 'cm'

    env['CM_DOCKER_IMAGE_NAME'] = docker_image_name

    if env.get("CM_DOCKER_IMAGE_TAG", "") == '':
        env['CM_DOCKER_IMAGE_TAG'] = "latest"

    if env.get("CM_DOCKER_CACHE", "yes") == "no":
        env["CM_DOCKER_CACHE_ARG"] = " --no-cache"

    return {'return':0}
