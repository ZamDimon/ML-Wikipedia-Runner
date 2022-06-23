import numpy as np
a = np.array([10216.0, 90068.0, 183172.0, 67754.0, 16317.0, 3738.0])
b = [0.616, 0.26, 0.076, 0.038, 0.008, 0.002]
a = a / sum(a)
print(a)
print(b)
print(a/b/6.4917455)