from typing import List, Optional, Dict
from collections.abc import Callable
from math import log
from bisect import *
from functools import cache, lru_cache
from collections import deque, defaultdict, Counter
from heapq import *
import heapq
from math import inf, isinf
import copy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
