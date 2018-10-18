log_parser.parse_nat_log returns dict
{
  "-DevIP" : "1.1.6.9", #生成日志设备IP
  "Protocol" : "TCP", #协议
  "Application" : "http", #应用
  "SrcIPAddr" : "222.196.185.195", #源地址、内部地址
  "SrcPort" : "54720", # 源端口
  "NatSrcIPAddr" : "117.173.86.3", #NAT后源地址，远端应用程序看到的地址
  "NatSrcPort" : "62139", #NAT后源端口
  "DstIPAddr" : "121.51.131.14", #目标地址
  "DstPort" : "80", #目标端口
  "NatDstIPAddr" : "121.51.131.14", #NAT后目标地址（反向NAT）
  "NatDstPort" : "80", #NAT后目标端口
  "InitPktCount" : "0", # 数据包数
  "InitByteCount" : "0", # 字节数
  "RplyPktCount" : "0", # 返回包数
  "RplyByteCount" : "0", # 返回字节数
  "RcvVPNInstance" : "", # 接收VPN实例，主要用于MPLS VPN
  "SndVPNInstance" : "", # 发送VPN实例
  "RcvDSLiteTunnelPeer" : "", # 接收端双栈（隧道）
  "SndDSLiteTunnelPeer" : "", # 发送端双栈隧道
  "BeginTime_e" : "10012018031545", # 会话建立时间
  "EndTime_e" : "", # 会话结束时间
  "Event" : "Sessioncreated", # NAT事件类型
  "time_stamp" : ISODate("2018-10-01T11:15:45Z"), #时间戳（设备上的）
  "device" : "F5020-BB-4J-3", # 设备名称
  "type" : "%%10NAT/6/NAT_FLOW" #Syslog日志类型
}
