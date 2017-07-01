modprobe v4l2_common && python cam-pir.py &
cd /data
python -m SimpleHTTPServer 80
