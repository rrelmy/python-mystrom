"""
Copyright (c) 2015-2016 Fabian Affolter <fabian@affolter-engineering.ch>

Licensed under MIT. All rights reserved.
"""
import requests


class MyStromPlug(object):
    """ A class for a myStrom switch. """

    def __init__(self, host):
        self.resource = 'http://{}'.format(host)
        self.timeout = 10
        self.data = None
        self.state = None
        self.consumption = None
        self.update()

    def set_relay_on(self):
        """ Turn the relay on. """
        if not self.get_relay_state():
            try:
                request = requests.get('{}/relay'.format(self.resource),
                                       params={'state': '1'},
                                       timeout=self.timeout)
                if request.status_code == 200:
                    self.update()
            except requests.exceptions.ConnectionError:
                print("Can't turn on %s.", self.resource)

    def set_relay_off(self):
        """ Turn the relay off. """
        if self.get_relay_state():
            try:
                request = requests.get('{}/relay'.format(self.resource),
                                       params={'state': '0'},
                                       timeout=self.timeout)
                if request.status_code == 200:
                    self.update()
            except requests.exceptions.ConnectionError:
                print("Can't turn on %s.", self.resource)

    def get_status(self):
        """ Gets the details from the switch. """
        try:
            request = requests.get('{}/report'.format(self.resource),
                                   timeout=10)
            self.data = request.json()
        except requests.exceptions.ConnectionError:
            print("No route to device: ", self.resource)
        except ValueError:
            print("No route to device: ", self.resource)

    def get_relay_state(self):
        """ Get the relay state. """
        self.update()
        try:
            self.state = self.data['relay']
        except TypeError:
            self.state = None

        return self.state

    def get_consumption(self):
        """ Get current power consumption in mWh. """
        self.update()
        try:
            self.consumption = self.data['power']
        except TypeError:
            self.consumption = 'N/A'

        return self.consumption

    def update(self):
        """ Get current details from switch. """
        return self.get_status()