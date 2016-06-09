"""
Initializes the GanjaBot with apikeys and starts it.
Will accept command line arguments in a future release.
"""
import ganja

client = ganja.GanjaClient('.apikeys', True)
client.run()
