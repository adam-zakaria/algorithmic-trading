#!/usr/bin/env python

# This file is part of krakenex.
# Licensed under the Simplified BSD license. See `examples/LICENSE.txt`.

# Prints the account blance to standard output.

import krakenex

k = krakenex.API(key="4wYNY5f9BHIpXXgPwyJ9/zmL5HERrxVZc8tZYhNSBayKc9gU/+vxoeLo", secret="E7WVxzKa5tiSGPd+/0x9dCCGTBVwrsmuEdxR3omgLigp5BVykg+P7VXoWIAI69/U9JLHRqH9gFwLLCsgEPMIzw==")

print(k.query_private('Balance'))