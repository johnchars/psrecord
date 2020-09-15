#!/usr/bin/python
import argparse

parser = argparse.ArgumentParser(
      description='Plot cpu usage')
parser.add_argument('--log', type=str,
                      help='source file including time cpu memory, etc')
parser.add_argument('--plot', type=str,
                      help='output the statistics to a plot')                      
args = parser.parse_args()
logfile = args.log
plot=args.plot
file = open(logfile, 'r')
lines = file.read().replace("\t"," ").split('\n')
list = [[v.strip() for v in line.split(" ") if v.strip()!=""] for line in lines if len(line)>0 and line[0]!="#"]
log = {}
log['times'] = []
log['cpu'] = []
log['mem_real'] = []
log['mem_virtual'] = []

for l in list:
	if len(l)>1:
		print(l)
		log['times'].append(float(l[0]))
		log['cpu'].append(float(l[1]))
		log['mem_real'].append(float(l[2]))
		log['mem_virtual'].append(float(l[3]))
file.close()  

import matplotlib.pyplot as plt
with plt.rc_context({'backend': 'Agg'}):

  fig = plt.figure()
  ax = fig.add_subplot(1, 1, 1)

  ax.plot(log['times'], log['cpu'], '-', lw=1, color='r')

  ax.set_ylabel('CPU (%)', color='r')
  ax.set_xlabel('time (s)')
  ax.set_ylim(0., max(log['cpu']) * 1.2)

  ax2 = ax.twinx()

  ax2.plot(log['times'], log['mem_real'], '-', lw=1, color='b')
  ax2.set_ylim(0., max(log['mem_real']) * 1.2)

  ax2.set_ylabel('Real Memory (MB)', color='b')

  ax.grid()

  fig.savefig(plot)