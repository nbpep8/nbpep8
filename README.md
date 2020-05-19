# ```nbpep8```

A package for PEP8 analysis in browser based Jupyter notebooks, such as Kaggle and Google Colabatory, that do not allow adding 3rd Party PEP8 analysis tools as add ons.


## Prerequisites

- Install ```pycodestyle``` if already not installed. This package replaces old ```pep8``` package. It comes pre-installed in Kaggle notebooks but not in Google Colabs.
- Install ```nbpep8``` from ```test.pypi ```. I will push to ```PyPI``` in future.

```
pip install pycodestyle
pip install --index-url https://test.pypi.org/simple/ nbpep8
```

## How to Use?

### Import ```nbpep8```

```
from nbpep8.nbpep8 import pep8
```

### Analysis
Add ```pep8(_ih)``` at the end of the code cell to see ```PEP8``` analysis.

Example:

```
import os
import sys


a=  23

pep8(_ih)
```

Output:

```
cell_content.py:5:2: E225 missing whitespace around operator
cell_content.py:5:3: E222 multiple spaces after operator
```

Any suggestions to improve? Please send me a message at https://www.linkedin.com/in/debanga/.

---
**(c) 2020, Debanga Raj Neog**
