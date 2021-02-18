# -*- coding: utf-8 -*-
import pandas as pd

ex = {'a' : [1, 2],
      'b' : [3, 4],
      'c' : ['d', 'e']}

ex = pd.DataFrame(ex)
print(ex['a'][0])
