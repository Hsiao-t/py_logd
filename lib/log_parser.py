"""
日志解析程序，定义日志解析程式，并在CALL_TBL调用表中作关联。
-- c_TBL 结构
-- c_TBL = {
--   "日志标签": [
--     处理函数, 参数表 #其中，处理函数要之前已经定义，参数表为dict或者list
--   ]
-- }
"""

import re

def _pre_handle(src):
  return re.sub(r'\(.*?\)','',src)

def _convert_to_record(src,sp_a=";",sp_b="="):
  src = _pre_handle(src)
  r = dict()
  a = src.split(sp_a)
  for _ in a:
    va = _.split(sp_b)
    r[va[0]] = "" if len(va)==1 else va[1]
  return r

def parse_nat(src,**kw_args):
  return _convert_to_record(src,**kw_args)

CALL_TBL = {

  "%%10NAT/6/NAT_FLOW": [
    parse_nat,
    {'sp_a':';','sp_b':'='}
  ],

}
