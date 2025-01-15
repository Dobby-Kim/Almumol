"""
title : Moving Average From Data Stream
link  : https://leetcode.com/problems/moving-average-from-data-stream

description

MovingAverage class의 next 메서드를 구현한다. 
next 메서드는 val을 받는다. next 메서드는 지금까지 받은 수의 평균값을 구한다.
단, 평균값은 최근 받은 size 이하의 수만 계산한다.

"""

from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()

    def next(self, val: int) -> float:
        while len(self.queue) >= self.size:
            self.queue.popleft()
        self.queue.append(val)
        return sum(self.queue) / len(self.queue)
        