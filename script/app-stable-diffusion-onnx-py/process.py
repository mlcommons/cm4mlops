# https://huggingface.co/runwayml/stable-diffusion-v1-5/tree/onnx

import os
import logging
from optimum.onnxruntime import ORTStableDiffusionPipeline

output = os.environ.get('CM_APP_STABLE_DIFFUSION_ONNX_PY_OUTPUT','')

f = os.path.join(output, 'output.png')

if os.path.isfile(f):
    os.remove(f)

cm_model_path = os.environ.get('CM_ML_MODEL_PATH','')
if cm_model_path == '':
    logging.info ('Error: CM_ML_MODEL_PATH env is not defined')
    exit(1)

device = os.environ.get('CM_DEVICE','')

pipeline = ORTStableDiffusionPipeline.from_pretrained(cm_model_path, local_files_only=True).to(device)

text = os.environ.get('CM_APP_STABLE_DIFFUSION_ONNX_PY_TEXT','')
if text == '': text = "a photo of an astronaut riding a horse on mars"


logging.info ('')
logging.info ('Generating imaged based on "{}"'.format(text))

image = pipeline(text).images[0]

image.save(f)

logging.info ('Image recorded to "{}"'.format(f))
