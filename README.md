# ChatGPT Linux和Windows系统IP可用性检测

由于ChatGPT开始封禁大量账号，并且有些服务器或者Windows已开代理ip不能注册或者使用，为了方便检测，同时为了在使用之前自查ip，避免被封帐号，以下两个命令分别对应Linux和Windows检测ip可用性，注意Windows尽量使用全局VPN，比如OpenVPN等代理到网络层（Network Layer）或者开启clash TUN模式。

***

# 使用说明

Linux安装并运行脚本

	wget -O chat_test.sh https://raw.githubusercontent.com/ZeroBit3/chatgpt_ip_test/main/chat_test.sh && chmod +x chat_test.sh && clear && ./chat_test.sh

