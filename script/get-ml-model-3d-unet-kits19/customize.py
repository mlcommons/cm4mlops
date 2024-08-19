from cmind import utils
import os
import hashlib

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    automation = i['automation']

    cm = automation.cmind

    path = os.getcwd()

    url = env['CM_PACKAGE_URL']

    # flag to turn on download
    download_file = False

    # md5 check
    if env['CM_ML_MODEL_FILE'] == "3dunet_kits19_128x128x128.tf":
        download_file_name = env['CM_ML_MODEL_FILE'] + ".zip"
    else:
        download_file_name = env['CM_ML_MODEL_FILE']
    download_file_path = os.path.join(path, download_file_name)
    if os.path.exists(download_file_path):
        md5_hash = hashlib.md5()
        with open(os.path.join(download_file_path), "rb") as file:
            for byte_block in iter(lambda: file.read(4096), b""):
                md5_hash.update(byte_block)
        calculated_hash = md5_hash.hexdigest()
        if calculated_hash == env['CM_DOWNLOAD_CHECKSUM']:
            print("The download file exists. Checksum verified.")
        else:
            print("The download file exists but is corruped. md5 checksum mismatch.")
            print("Deleting and downloading the file again.")
            os.remove(download_file_path)
            download_file = True
    else:
        download_file = True
    
    if download_file:
        print ('Downloading from {}'.format(url))

        r = cm.access({'action':'download_file', 
                   'automation':'utils,dc2743f8450541e3', 
                   'url':url})
        if r['return']>0: return r

        filename = r['filename']

    # Developer note:
    # Currently, the md5 hash given in https://zenodo.org/records/5597155 for file 3dunet_kits19_128x128x128.tf.zip
    # is for the zip file not the model file inside the zip. The below code is written with the assumption that
    # extracted files are currupted if the md5 check of zip is successfull but the script is not loaded from cache.
    if not download_file:
        filename = download_file_path 
    if env.get('CM_UNZIP') == "yes":
            os.system("unzip -o "+filename)
            filename = env['CM_ML_MODEL_FILE']
            env['CM_ML_MODEL_FILE_WITH_PATH']=os.path.join(path, filename)
    else:
            # Add to path
            env['CM_ML_MODEL_FILE']=filename
            env['CM_ML_MODEL_FILE_WITH_PATH']=os.path.join(path, filename)

    env['CM_ML_MODEL_PATH']=path

    return {'return':0}
