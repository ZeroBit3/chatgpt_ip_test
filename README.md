# ChatGPT Linux和Windows系统IP可用性检测

由于ChatGPT开始封禁大量账号，并且有些服务器或者Windows已开代理ip不能注册或者使用，为了方便检测，同时为了在使用之前自查ip，避免被封帐号，以下两个命令分别对应Linux和Windows检测ip可用性，注意Windows尽量使用全局VPN，比如OpenVPN等代理到网络层（Network Layer）或者开启clash TUN模式。

***

# 使用说明

Linux安装并运行脚本

	wget -O chat_test.sh https://raw.githubusercontent.com/ZeroBit3/chatgpt_ip_test/main/chat_test.sh && chmod +x chat_test.sh && clear && ./chat_test.sh

Windows安装并运行脚本(此脚本需要提前安装curl ：https://curl.se/windows/），以下命令适用于使用VPN协议的用户，比如OpenVPN等。

![curl](https://github.com/ZeroBit3/chatgpt_ip_test/assets/49831656/faf1b5de-985a-4a8c-9ad3-6a9036bb724d)

到脚本目录cmd执行

	python ip_test_VPN.py
 
Windows安装并运行脚本（此脚本也需要安装curl ：https://curl.se/windows/）
以下命令适用于使用clash，v2ray机场节点的用户，但是要更改py文件中最后的代理ip和端口，默认7890是clash默认端口，请自行修改）。

到脚本目录cmd执行

	python ip_test_software.py

 ![修改](https://github.com/ZeroBit3/chatgpt_ip_test/assets/49831656/22c12f47-1cbe-4122-82ca-18c3e89bbd40)
