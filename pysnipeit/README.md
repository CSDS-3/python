# SNIPE_IT API

Install this module with PIP. Credentials to SNIPE_IT should be passed into the constructor,   

```
from pysnipeit import SnipeIT
snipe = SnipeIT(base_url=x,token=y)
```
.. or configured as env vars SNIPE_URL, SNIPE_TOK  

```
setx SNIPE_URL x
setx SNIPE_TOK y
# restart terminal
from pysnipeit import SnipeIT
snipe = SnipeIT()
```
