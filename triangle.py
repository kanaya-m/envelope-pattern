
"""
Created on Sat Feb 27 10:31:29 2021

@author: Kanaya Malakar
"""

import matplotlib.pyplot as plt
import envelop as env

# Triangle with each side having 20 segments
E1 = env.Envelope(3, segments=20) 
# Join margins 1 and 2 with blue lines
E1.join_margins(1, 2, color='blue') 
# Join margins 2 and 3 with seagreen lines
E1.join_margins(2, 3, color='seagreen')
# Join margins 3 and 1 with yellow lines in reverse order.
E1.join_margins(3, 1, color='yellow', reverse=True)

# Plot bounding polygon
e1 = (E1.upright_polygon())
plt.plot(e1[:, 0], e1[:, 1], 'bo')
plt.axis('off')
#plt.savefig('fig8.png')
plt.show()