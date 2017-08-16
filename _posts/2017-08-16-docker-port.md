---
layout: github
title: docker端口冲突小记
---

# docker端口冲突小记

## 事件起因

前几天把我的装有显卡的服务器共享给另外的同学，这位同学复用了我的镜像，产生了新的容器，启动容器时候把容器里的8888端口映射到host机器的8888端口了。导致的结果就是我的之前的容器因为同样绑定到host机器8888端口，所以启动不了：

```
Error response from daemon: ......

Bind for 0.0.0.0:8888 failed: port is already allocated
```

我不想停掉这位同学的容器，但我自己的容器里也有一些文件我不想丢弃，所以也不能放弃这个容器，另外启动一个新的重新绑定端口。

## 方案

方案也挺简单，首先把我的容器制作一个新的镜像

```
sudo docker commit containerid name/imagename
```

然后用新的镜像建立一个容器

```
sudo nvidia-docker run -itd -P  name/imagename
```

因为我的容器并不是对外提供服务的，只是自己练手的，所以这次学乖了不再绑定到host固定的端口了，来避免后续的端口冲突的问题。可以通过docker port命令来查询绑定的host端口

```
luolei@ubuntu:~$ sudo docker port new_container_id
6006/tcp -> 0.0.0.0:32783
8888/tcp -> 0.0.0.0:32782
```

最后再把旧的端口冲突的容器删除掉

```
luolei@ubuntu:~$ sudo docker rm old_container_id
```

至此误伤完成端口切换：）