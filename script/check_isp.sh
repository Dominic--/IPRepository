#/bin/bash

echo "验证新IPB数据和旧有ISP数据的重合度..."
python ./script/python/check_isp.py ./tmp/ip.isp ./data/ip.type ./tmp/conflict.ip
