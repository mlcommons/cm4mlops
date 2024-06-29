from sparsezoo import Model
import os
import logging
model_stub= os.environ.get('CM_MODEL_ZOO_STUB', '')
logging.info(f"Downloading model {model_stub}")
stub = f"{model_stub}"
model = Model(stub)

with open('tmp-run-env.out', 'w') as f:
    f.write(f"CM_ML_MODEL_FILE_WITH_PATH={model.path}")
