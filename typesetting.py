#!/usr/bin/env python
#
# -*- coding: utf-8 -*-

from sys import maxint as INF
from sys import argv
import os

# INF = NaN

def is_number(s):
  try:
    int(s)
    return True
  except ValueError:
    return False

def linecost(n,M,i,j,lenghts):
  """
  Linear cost of extra caracters until fill up the line.
  :param n: number of words
  :param M: maximum caracters per word
  """
  extras = M - j + i - sum(lenghts[i:j+1])
  if extras < 0:
    # Doesn't fit in line
    return INF
  if j==n-1 :
    # Last line
    return 0
  else:
    return extras**2

def dynamic_typeset(n,M,last,lengths):

  best=[0 for _ in range(n)] # Auxiliary vector for best cost
  i=j=n-1
  while(linecost(n,M,i,j,lengths)!=INF):
    best[i]=linecost(n,M,i,j,lengths)
    last[i]=n
    # print " ".join(map(str,best))
    # print "-".join(map(str,last))
    i-=1

  while i>=0:
    # print " ".join(map(str,best))
    # print "-".join(map(str,last))
    min_cost = INF
    lessk = n
    for k in range(n-1,i,-1):
      c = linecost(n,M,i,k-1,lengths)
      if(c==INF):
        continue
      c += best[k]
      if c < min_cost:
        min_cost = c
        lessk = k
      # print "{} cost({},{})={}+{}={}".format(min_cost,i-2,k,linecost(n,M,i-2,k,lengths),best[k],linecost(n,M,i-2,k,lengths)+best[k])
    best[i] = min_cost
    last[i] = lessk
    i -= 1

  return best[0]

def to_lines(n,p,words):
    lines=[]
    i = 0
    while i < n:
      j = p[i]# last[]
      lines.append(words[i:j])
      i = j
    return lines

def typeset(words,m):

  # TODO: paso la lista de palabras a lista de longitudes de palabras
  l = [len(word) for word in words]

  if not words:
      raise IOError("No se han introducido palabras")

  if max(l) > m:
      raise IOError("Margen inferior a la longitud por palabra(%d,%d)"%(max(l),m))

  # Numero de palabras
  n = len(words)

  mA = [[INF for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(i,n):
      mA[i][j]=linecost(n,m,i,j,l)

  # TODO: calculo coste total
  p = [0 for _ in range(n)]
  # print "-".join(map(str,p))
  print dynamic_typeset(n,m,p,l)
  # print "-".join(map(str,p))

  #return
  # TODO: construimos el parrafo desde el principio al final
  lines = to_lines(n,p,words)

  text = ""

  for line in lines:
    text += " ".join(line)+"\n"
    print "%3d"%len(" ".join(line))," ".join(line)

  return text

if __name__ == '__main__':
  main()
