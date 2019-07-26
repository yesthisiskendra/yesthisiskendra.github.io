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

if __name__ == '__main__':
  fptr = open('input1.txt', 'r')

  input_arr = []
  for line in fptr:
    input_arr.append(line.split())

  get_bodies(input_arr)
  fptr.close()
