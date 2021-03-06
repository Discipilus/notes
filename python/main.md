# External Libraries

## GDAL
```bash
gdal-config --version
gdal-config --cflags
```

Here we get path where C/C++ headers are located
Setup envs with this path:
```bash
export CPLUS_INCLUDE_PATH=/usr/local/include/
export C_INCLUDE_PATH=/usr/local/include/
``` 

Build GDAL:
```bash
cmake -DPython_LOOKUP_VERSION=3.11 ..
cmake --build .
sudo cmake --build . --target install
```












