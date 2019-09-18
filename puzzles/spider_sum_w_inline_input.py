#!/bin/python3

import math
import os
import random
import re
import sys

def get_spider_sum(arr, body1, body2):
  sum = int(arr[body1-1][body2-1]) + int(arr[body1-1][body2]) + int(arr[body1-1][body2+1]) \
    + int(arr[body1][body2]) \
    + int(arr[body1+1][body2-1]) + int(arr[body1+1][body2]) + int(arr[body1+1][body2+1]) 
  return(sum)
  print(body1, body2)

def get_bodies(arr):
  totals = []
  for i in range(1,len(arr)-1):
    for j in range(1,len(arr[i]) -1):
      totals.append(get_spider_sum(arr,i,j))
  print(sorted(totals).pop())

input_array = [['1', '1', '1', '0', '0', '0'], ['0', '1', '0', '0', '0', '0'], ['1', '1', '1', '0', '0', '0'], ['0', '0', '2', '4', '4', '0'], ['0', '0', '0', '2', '0', '0'], ['0', '0', '1', '2', '4', '0']]
get_bodies(input_array)