#!/bin/bash
source /opt/conda/etc/profile.d/conda.sh
/opt/conda/bin/activate /opt/conda/envs/pytorch
/home/ubuntu/.local/bin/waitress-serve --host 0.0.0.0 --port 5000 app:app
