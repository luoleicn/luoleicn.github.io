---
layout: github
title: Java内存泄漏分析
---

# Java内存泄漏分析

某日，客户抱怨系统非常卡顿，影响了正常作业。根据现象怀疑是后台数据库查询慢，看了下查询日志确实验证了这一点，top了下，发现后台系统CPU占用率奇高，内存占用也很大，所以就想看下哪个线程消耗了过多资源。
	
使用下面命令，可以查询到线程级别的信息
	
	ps -mp pid -o THREAD,tid,time


结果如下图
![image](http://www.luolei.info/source/images/ps.jpg)

发现有很多线程都没有占用cpu，而有一些线程很相似，如线程57804，都占用了相同的cpu，接着用jstack去dump下线程的堆栈
	
	jstack pid

结果如下图
![image](http://www.luolei.info/source/images/jstack.jpg)

在dump出来的java堆栈信息中没有找到线程57804的信息，于是又使用到了linux命令查线程堆栈
	
	pstack pid

结果如下图![image](http://www.luolei.info/source/images/pstack.jpg)

这回找到线程57804，果然跟设想的一样，是因为内存占用太高，导致系统在不停的执行垃圾回收，导致系统性能很低，应该是哪里的代码有问题，导致了内存泄漏。于是用jmap尝试把内存信息dump出来

	jmap -dump:format=b,file=heap.bin pid

结果发现或许是因为系统资源占用太多，gc太频繁，jmap特别慢，没办法为了不影响作业只得直接重启系统。后来去了另一个环境，这个环境下系统也跑了很久，但还没有出现频繁GC的情况，于是在这个环境中用jmap把内存dump出来了。

接下来用[Eclipse Memory Analyzer](http://www.eclipse.org/mat/) 分析内存文件，可以看到有4G的大对象：

![image](http://www.luolei.info/source/images/jprofile1.jpg)

点击对象进行分析：

![image](http://www.luolei.info/source/images/jprofile2.jpg)

定位到一个hashset对象占有4G内存，这个是不合理的，于是发现了内存泄漏的原因，修复了问题。

### Ref
1）[http://www.blogjava.net/hankchen/archive/2012/05/09/377735.html](http://www.blogjava.net/hankchen/archive/2012/05/09/377735.html)

