"""
Syslog 日志格式定义
"""

LOG_SERVERITY = {
  0: "Emerg",
  1: "Alert",
  2: "Critcal",
  3: "Error",
  4: "Warning",
  5: "Notice",
  6: "Info",
  7: "Debug",
}

LOG_FACILITY = {
  0: "Kernel",
  1: "User",
  2: "Mail",
  3: "System daemon",
  4: "Security",
  5: "Internally",
  6: "Line Printer",
  7: "Network News subsystem",
  8: "UUCP subsystem",
  9: "Clock daemon",
  10: "Security",
  11: "FTP daemon",
  12: "NTP subsystem",
  13: "LOG Audit",
  14: "LOG Alert",
  15: "Clock daemon",
  16: "Local-0",
  17: "Local-1",
  18: "Local-2",
  19: "Local-3",
  20: "Local-4",
  21: "Local-5",
  22: "Local-6",
  23: "Local-7",
}
from time import strptime
from datetime import datetime

class Syslog_t(object):
  def __init__(s,msg,tf=20,with_tag=True):
    """
    Input:
      msg -- syslog原始文本
      tf -- 日期字符串长度,15位则代表 MMM DD HH:MM:SS, 20位则代表 MMM DD HH:MM:SS YYYY
    Output:
      初始化方法，无
    """
    cy = datetime.now().year
    i_pri = int(msg[msg.find("<")+1:msg.find(">")])
    s.SERVERITY = LOG_SERVERITY[i_pri&7]
    s.FACILITY = LOG_FACILITY[i_pri>>3]
    i_time = msg[msg.find(">")+1:msg.find(">")+tf+1] if tf == 20 else msg[msg.find(">")+1:msg.find(">")+tf+1] + " " + str(cy)
    _ts = strptime(i_time,"%b %d %H:%M:%S %Y")
    s.DATETIME = datetime(
      _ts.tm_year,
      _ts.tm_mon,
      _ts.tm_mday,
      _ts.tm_hour,
      _ts.tm_min,
      _ts.tm_sec
    )
    _msg = msg[msg.find(">")+tf+2:]
    s.DEVICE = _msg[:_msg.find(" ")]
    if with_tag:
      s.TAG = _msg[_msg.find(" ")+1:_msg.find(":")]
      s.MSG = _msg[_msg.find(":")+2:]
    else:
      s.TAG = "-/-"
      s.MSG = _msg
