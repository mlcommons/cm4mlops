rem call this script with computer_mouse.jpg as input

call 0-common.bat

docker run -v %CD%:/tmp/host -it --rm cknowledge/cm-script-app-image-classification-onnx-py:ubuntu-23.04-latest -c "time cmr 'python app image-classification onnx' --adr.python.name=cm --input=/tmp/host/%1"
