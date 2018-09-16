"""
Copyright (c) 2018 Rémy Böhler <git@rrelmy.ch>

Licensed under MIT. All rights reserved.
"""

from pymystrom import switch

plug = switch.MyStromPlug('10.100.0.137')

# Get the new state of the switch
temperature = plug.get_temperature()
print("Temperature measured:", temperature['measured'])
print("Temperature compensation:", temperature['compensation'])
print("Temperature compensated:", temperature['compensated'])
