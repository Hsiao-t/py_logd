LOG_PARSE_PTM = {

  "ppp_abnml":{
    "tb_name": "ppp_abnml",
    "db_eng": "postgresql://dbo:@localhost/loga",
    "c_names": ["date","time","device","slot","username","ip_address","ifname","s_vlan","c_vlan","usermac","reason","msg"],
    "parse_pattern": "(.*?)T(.*?)\\+.*?PPP/6/PPP_USER_LOGOFF_ABNORMAL: -DevIP=(.*?)-Slot=(.*?); -UserName=(.*?)-IPAddr=(.*?)-IfName=(.*?)-OuterVLAN=(.*?)-InnerVLAN=(.*?)-MACAddr=(.*?)-Reason=(.*?); (.*?)"
  },

  "ppp_fail":{
    "tb_name": "ppp_fail",
    "db_eng": "postgresql://dbo:@localhost/loga",
    "c_names": ["date","time","device","slot","username","ip_address","ifname","s_vlan","c_vlan","usermac","reason_num","reason_msg","msg"],
    "parse_pattern": "(.*?)T(.*?)\\+.*?PPP/6/PPP_USER_LOGON_FAILED: -DevIP=(.*?)-Slot=(.*?); -UserName=(.*?)-IPAddr=(.*?)-IfName=(.*?)-OuterVLAN=(.*?)-InnerVLAN=(.*?)-MACAddr=(.*?)-Reason=(.*?): (.*?); (.*?)"
  },

  "wlan_sta_on":{
    "tb_name": "wlan_sta",
    "db_eng": "postgresql://dbo:@localhost/loga",
    "c_names": ["date","time","device","usermac","bssid","essid","apname","newstat"],
    "parse_pattern": "(.*?)T(.*?)\\+.*?STAMGR/6/STAMGR_CLIENT_ONLINE: -DevIP=(.*?); Client (.*?) went online from BSS (.*?) with SSID (.*?) on AP (.*?). State changed to (.*?)"
  },

  "wlan_sta_off":{
    "tb_name": "wlan_sta",
    "log": "/opt/log/wlan_station.log",
    "db_eng": "postgresql://dbo:@localhost/loga",
    "c_names": ["date","time","device","usermac","bssid","essid","apname","newstat"],
    "parse_pattern": "(.*?)T(.*?)\\+.*?STAMGR/6/STAMGR_CLIENT_OFFLINE: -DevIP=(.*?); Client (.*?) went offline from BSS (.*?) with SSID (.*?) on AP (.*?). State changed to (.*?). Reason:.*?"
  },

  "wlan_sta_snooping":{
    "tb_name": "wlan_sta_sp",
    "log": "/opt/log/wlan.log",
    "db_eng": "postgresql://dbo:@localhost/loga",
    "c_names": ["date","time","device","usermac","ip1","ip2","ip3","ip4","username","apname","radio","channel","essid","bssid"],
    "parse_pattern": "(.*?)T(.*?)\\+.*?STAMGR/6/STAMGR_CLIENT_SNOOPING: -DevIP=(.*?); Detected client IP change: Client MAC: (.*?), IP: (.*?), (.*?), (.*?), (.*?), Username: (.*?),  AP name: (.*?), Radio ID: (.*?), Channel number: (.*?), SSID: (.*?), BSSID: (.*?)\\."
  },

  "wlan_ap_stat_on":{
    "tb_name": "wlan_ap_stat",
    "log": "/opt/log/wlan_ap_stat.log",
    "db_eng": "postgresql://dbo:@localhost/loga",
    "c_names": ["date","time","device","apname","newstat"],
    "parse_pattern": "(.*?)T(.*?)\\+.*?CWS/6/CWS_AP_UP: -DevIP=(.*?); Master CAPWAP tunnel to AP (.*?) went (.*?)\\."
  },

  "wlan_ap_stat_idle":{
    "tb_name": "wlan_ap_stat",
    "log": "/opt/log/wlan_ap_stat.log",
    "db_eng": "postgresql://dbo:@localhost/loga",
    "c_names": ["date","time","device","apname","newstat"],
    "parse_pattern": "(.*?)T(.*?)\\+.*?CWS/4/CWS_AP_DOWN: -DevIP=(.*?); CAPWAP tunnel to AP (.*?) went (.*?). Reason: .*?\\."
  },

  "%%10DOT1X/5/DOT1X_WLAN_LOGIN_FAILURE":{
    "tb_name": "wlan_dot1x_auth",
    "log": "/opt/log/wlan_dot1x.log",
    "db_eng": "postgresql://dbo:@localhost/loga",
    "c_names": ["date","time","device","username","usermac","bssid","essid","vlanid","newstat"],
    "parse_pattern": "(.*?)T(.*?)\\+.*?DOT1X/5/DOT1X_WLAN_LOGIN_FAILURE: -DevIP=(.*?); -Username=(.*?)-UserMAC=(.*?)-BSSID=(.*?)-SSID=(.*?)-VLANID=(.*?); A user (.*?) 802.1X authentication\\."
  },
    
  "%%10DOT1X/6/DOT1X_WLAN_LOGIN_SUCC":{
    "tb_name": "wlan_dot1x_auth",
    "log": "/opt/log/wlan_dot1x.log",
    "db_eng": "postgresql://dbo:@localhost/loga",
    "c_names": ["device","username","usermac","bssid","essid","vlanid","newstat"],
    "parse_pattern": "-DevIP=(.*?); -Username=(.*?)-UserMAC=(.*?)-BSSID=(.*?)-SSID=(.*?)-VLANID=(.*?); A user passed 802.1X authentication and came (.*?)\\."
  },

  "%%10DOT1X/6/DOT1X_WLAN_LOGOFF":{
    "tb_name": "wlan_dot1x_auth",
    "log": "/opt/log/wlan_dot1x.log",
    "db_eng": "postgresql://dbo:@localhost/loga",
    "c_names": ["device","username","usermac","bssid","essid","vlanid","newstat"],
    "parse_pattern": "-DevIP=(.*?); -Username=(.*?)-UserMAC=(.*?)-BSSID=(.*?)-SSID=(.*?)-VLANID=(.*?); Session for an 802.1X user was (.*?)\\."
  },

  "%%10PPP/6/PPP_USER_LOGON_SUCCESS":{
    "tb_name": "ppp_nml",
    "log": "/opt/log/ppp_login_succ.log",
    "db_eng": "postgresql://dbo:@localhost/loga",
    "c_names": ["device","slot","user","ip","ifname","s_vlan","c_vlan","mac"],
    "parse_pattern": "-DevIP=(.*?)-Slot=(.*?); -UserName=(.*?)-IPAddr=(.*?)-IfName=(.*?)-OuterVLAN=(.*?)-InnerVLAN=(.*?)-MACAddr=(.*?); The user came online successfully\\."
  },

  "%%10PPP/6/PPP_USER_LOGOFF":{
    "tb_name": "ppp_nml",
    "db_eng": "postgresql://dbo:@localhost/loga",
    "c_names": ["device","slot","user","ip","ifname","s_vlan","c_vlan","mac"],
    "parse_pattern": "-DevIP=(.*?)-Slot=(.*?); -UserName=(.*?)-IPAddr=(.*?)-IfName=(.*?)-OuterVLAN=(.*?)-InnerVLAN=(.*?)-MACAddr=(.*?)-Reason=.*?\\."
  },

}

