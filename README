# Syslog 日志接收与处理简易程序

## 运行环境:
1) 在CentOS 6.5上测试
2) 本地安装并运行mongod服务程式
3) Python 3.6及以上版本
--> 安装 pymongo 模块
--> 安装 socketserver 模块

## 功能:
1) 从指定端口接收syslog日志并存储在mongodb数据库中
2) 可以定义syslog处理函数（须要懂Python）
3) 自带了H3C NAT日志处理程序

## 数据结构定义
必有字段:
1) time_stamp: 日志时间戳
2) device: 发送日志的设备IP或者主机名
3) type: 日志类别，从syslog中获得的TAG,如果没有，则自动添加为"-/-"
或有字段:
1) msg: 原始日志消息

如果应用程序定义了处理程序，日志会被划分为多个字段存储到数据库，具体参见相关文档,关于日志解析程式的定义位于:
-- syslogd/doc/parsers

启动命令: python logd
