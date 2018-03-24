# -*- coding=utf-8
'''
Created on 2016年9月23日

@author: zhaol
'''
from majiang2.table_state.state import MTableState
from freetime5.util import ftlog

class MTableStateXueliu(MTableState):
    
    def __init__(self):
        super(MTableStateXueliu, self).__init__()
        # 血战玩法
        self.setState(MTableState.TABLE_STATE_DROP)
        # 碰
        self.setState(MTableState.TABLE_STATE_PENG)
        # 杠
        self.setState(MTableState.TABLE_STATE_GANG)
        # 听
        self.setState(MTableState.TABLE_STATE_TING)
        #掷骰子
        self.setState(MTableState.TABLE_STATE_SAIZI)
        # 定缺
        self.setState(MTableState.TABLE_STATE_ABSENCE)
        # 抢杠胡
        self.setState(MTableState.TABLE_STATE_QIANGGANG)
        # 和
        self.setState(MTableState.TABLE_STATE_HU)
        # 和牌后血流成河
        self.setState(MTableState.TABLE_STATE_XUELIU)
        
    def getStandUpSchedule(self, state = MTableState.TABLE_STATE_NONE):
        """获取每一小局的发牌流程
        换三张 -> 定缺 
        """
        ftlog.debug('MTableStateXueliu.getStandUpSchedule state:', state,'states', self.states)
        if state == MTableState.TABLE_STATE_NONE:
            if self.states & MTableState.TABLE_STATE_SAIZI:
                ftlog.debug('MTableStateXueliu.getStandUpSchedule return ShaiZi')
                return MTableState.TABLE_STATE_SAIZI
    
            ftlog.debug('MTableStateXueliu.getStandUpSchedule return Next')
            return MTableState.TABLE_STATE_NEXT
    
        ftlog.debug('MTableStateXueliu.getStandUpSchedule return Next')
        return MTableState.TABLE_STATE_NEXT
        
