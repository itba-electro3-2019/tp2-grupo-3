import matplotlib.pyplot as plt
import numpy as np

def my_lines(ax, pos, *args, **kwargs):
    if ax == 'x':
        for p in pos:
            plt.axvline(p, *args, **kwargs)
    else:
        for p in pos:
            plt.axhline(p, *args, **kwargs)

clk=[1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]
t = np.arange(len(clk))

q0=[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0]
q1=[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0]
q2=[1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0]
q3=[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]

my_lines('x', range(len(clk)), color='.5', linewidth=1)
my_lines('y', [0, 2, 4, 6, 8], color='.5', linewidth=1)

plt.step(t, [i + 8 for i in clk] , 'g', linewidth = 2, where='post')
plt.text(t[0]-1.6, clk[0]+8.5, "CLK")

plt.step(t, [i + 6 for i in q0] , 'b', linewidth = 2, where='post')
plt.text(t[0]-1.5, q0[0]+6.5, "Q0")
plt.text(t[1]+0.15, q0[0]+5.2, '1')
plt.text(t[10]+0.25, q0[10]+6.4, '0')

plt.step(t, [i + 4 for i in q1] , 'b', linewidth = 2, where='post')
plt.text(t[0]-1.5, q1[0]+4.5, "Q1")
plt.text(t[1]+0.15, q1[0]+3.2, '1')
plt.text(t[11]+0.25, q1[11]+4.4, '0')

plt.step(t, [i + 2 for i in q2] , 'b', linewidth = 2, where='post')
plt.text(t[0]-1.5, q2[0]+2.5, "Q2")
plt.text(t[1]+0.15, q2[0]+1.2, '1')
plt.text(t[12]+0.25, q2[12]+2.4, '0')

plt.step(t, [i + 0 for i in q3] , 'b', linewidth = 2, where='post')
plt.text(t[0]-1.5, q2[0]+0.5, "Q3")
plt.text(t[1]+0.15, q3[0]-0.7+1, '0')
plt.text(t[13]+0.26, q3[13]-0.63, '1')

plt.ylim([-1,10])

plt.gca().axis('off')
plt.show()