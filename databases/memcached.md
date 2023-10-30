# Memcached
```shell
sudo apt install libmemcached-tools
memcdump --servers=127.0.0.1 | less
memccat --servers=127.0.0.1 SOME_KEY
for key in $(memcdump --server=127.0.0.1); do echo ------ $key ------; memccat --servers=127.0.0.1 $key; done

memcflush --server=127.0.0.1
```
