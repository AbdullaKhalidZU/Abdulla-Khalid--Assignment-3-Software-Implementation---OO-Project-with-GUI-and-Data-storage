# -*- coding: utf-8 -*-
"""Venue class

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16VnVbIBndsO298dgjBYgxh3V16MO2uzT
"""

class Venue:
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        self._venue_id = venue_id
        self._name = name
        self._address = address
        self._contact = contact
        self._min_guests = min_guests
        self._max_guests = max_guests

    # Getter and Setter methods
    def get_venue_id(self):
        return self._venue_id

    def set_venue_id(self, venue_id):
        self._venue_id = venue_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    def get_contact(self):
        return self._contact

    def set_contact(self, contact):
        self._contact = contact

    def get_min_guests(self):
        return self._min_guests

    def set_min_guests(self, min_guests):
        self._min_guests = min_guests

    def get_max_guests(self):
        return self._max_guests

    def set_max_guests(self, max_guests):
        self._max_guests = max_guests