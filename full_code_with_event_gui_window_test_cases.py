# -*- coding: utf-8 -*-
"""Full code with Event GUI window test cases

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19bErTNEqE2vm-1V3BZ9B1JxU1ZBSNKLi
"""

import tkinter as tk
from tkinter import messagebox



class Employee:
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details):
        self._name = name
        self._employee_id = employee_id
        self._department = department
        self._job_title = job_title
        self._basic_salary = basic_salary
        self._age = age
        self._date_of_birth = date_of_birth
        self._passport_details = passport_details

    def calculate_salary(self):
        # Basic implementation, can be extended for specific job titles
        return self._basic_salary

    # Getter and Setter methods
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_employee_id(self):
        return self._employee_id

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    def get_department(self):
        return self._department

    def set_department(self, department):
        self._department = department

    def get_job_title(self):
        return self._job_title

    def set_job_title(self, job_title):
        self._job_title = job_title

    def get_basic_salary(self):
        return self._basic_salary

    def set_basic_salary(self, basic_salary):
        self._basic_salary = basic_salary

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_date_of_birth(self):
        return self._date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    def get_passport_details(self):
        return self._passport_details

    def set_passport_details(self, passport_details):
        self._passport_details = passport_details


class Manager(Employee):
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details):
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self._team_managed = []

    def get_team_managed(self):
        return self._team_managed

    def add_employee(self, employee):
        self._team_managed.append(employee)

    def remove_employee(self, employee):
        self._team_managed.remove(employee)


class Salesperson(Employee):
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details):
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self._manager = None

    def get_manager(self):
        return self._manager

    def set_manager(self, manager):
        self._manager = manager


class Client:
    def __init__(self, client_id, name, address, contact_details, budget):
        self._client_id = client_id
        self._name = name
        self._address = address
        self._contact_details = contact_details
        self._budget = budget

    # Getter and Setter methods
    def get_client_id(self):
        return self._client_id

    def set_client_id(self, client_id):
        self._client_id = client_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    def get_contact_details(self):
        return self._contact_details

    def set_contact_details(self, contact_details):
        self._contact_details = contact_details

    def get_budget(self):
        return self._budget

    def set_budget(self, budget):
        self._budget = budget


class Supplier:
    def __init__(self, supplier_id, name, address, contact_details):
        self._supplier_id = supplier_id
        self._name = name
        self._address = address
        self._contact_details = contact_details

    # Getter and Setter methods
    def get_supplier_id(self):
        return self._supplier_id

    def set_supplier_id(self, supplier_id):
        self._supplier_id = supplier_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    def get_contact_details(self):
        return self._contact_details

    def set_contact_details(self, contact_details):
        self._contact_details = contact_details


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


class Event:
    def __init__(self, event_id, type, theme, date, time, duration, venue, client, guest_list, catering_company,
                 cleaning_company, decorations_company, entertainment_company, furniture_company, invoice):
        self._event_id = event_id
        self._type = type
        self._theme = theme
        self._date = date
        self._time = time
        self._duration = duration
        self._venue = venue
        self._client = client
        self._guest_list = guest_list
        self._catering_company = catering_company
        self._cleaning_company = cleaning_company
        self._decorations_company = decorations_company
        self._entertainment_company = entertainment_company
        self._furniture_company = furniture_company
        self._invoice = invoice

    # Getter and Setter methods
    def get_event_id(self):
        return self._event_id

    def set_event_id(self, event_id):
        self._event_id = event_id

    def get_type(self):
        return self._type

    def set_type(self, type):
        self._type = type

    def get_theme(self):
        return self._theme

    def set_theme(self, theme):
        self._theme = theme

    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date

    def get_time(self):
        return self._time

    def set_time(self, time):
        self._time = time

    def get_duration(self):
        return self._duration

    def set_duration(self, duration):
        self._duration = duration

    def get_venue(self):
        return self._venue

    def set_venue(self, venue):
        self._venue = venue

    def get_client(self):
        return self._client

    def set_client(self, client):
        self._client = client

    def get_guest_list(self):
        return self._guest_list

    def add_guest(self, guest):
        self._guest_list.append(guest)

    def remove_guest(self, guest):
        self._guest_list.remove(guest)

    def get_catering_company(self):
        return self._catering_company

    def set_catering_company(self, catering_company):
        self._catering_company = catering_company

    def get_cleaning_company(self):
        return self._cleaning_company

    def set_cleaning_company(self, cleaning_company):
        self._cleaning_company = cleaning_company

    def get_decorations_company(self):
        return self._decorations_company

    def set_decorations_company(self, decorations_company):
        self._decorations_company = decorations_company

    def get_entertainment_company(self):
        return self._entertainment_company

    def set_entertainment_company(self, entertainment_company):
        self._entertainment_company = entertainment_company

    def get_furniture_company(self):
        return self._furniture_company

    def set_furniture_company(self, furniture_company):
        self._furniture_company = furniture_company

    def get_invoice(self):
        return self._invoice

    def set_invoice(self, invoice):
        self._invoice = invoice


class Guest:
    def __init__(self, guest_id, name, address, contact_details):
        self._guest_id = guest_id
        self._name = name
        self._address = address
        self._contact_details = contact_details

    # Getter and Setter methods
    def get_guest_id(self):
        return self._guest_id

    def set_guest_id(self, guest_id):
        self._guest_id = guest_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    def get_contact_details(self):
        return self._contact_details

    def set_contact_details(self, contact_details):
        self._contact_details = contact_details


class ManagementApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Management System")

        self.label = tk.Label(master, text="Event ID:")
        self.label.grid(row=0, column=0)

        self.entry = tk.Entry(master)
        self.entry.grid(row=0, column=1)

        self.add_event_button = tk.Button(master, text="Add Event", command=self.add_event)
        self.add_event_button.grid(row=1, column=0)

        self.delete_event_button = tk.Button(master, text="Delete Event", command=self.delete_event)
        self.delete_event_button.grid(row=1, column=1)

        self.modify_event_button = tk.Button(master, text="Modify Event", command=self.modify_event)
        self.modify_event_button.grid(row=1, column=2)

        self.display_event_button = tk.Button(master, text="Display Event", command=self.display_event)
        self.display_event_button.grid(row=1, column=3)

        # List to store event instances
        self.events = []

        # Initialize events from provided data
        self.initialize_events()

    def initialize_events(self):
        # Initialize events from provided data
        # Event data provided: event_id, type, theme, date, time, duration, venue, client, guest_list, catering_company,
        # cleaning_company, decorations_company, entertainment_company, furniture_company, invoice
        event_data = [
            (1, "Wedding", "Romantic", "2024-05-15", "10:00", 6, "Venue A", "Client A", ["Guest 1", "Guest 2"],
             "Catering A", "Cleaning A", "Decorations A", "Entertainment A", "Furniture A", "Invoice A"),
            (2, "Conference", "Tech", "2024-06-20", "09:00", 8, "Venue B", "Client B", ["Guest 3", "Guest 4"],
             "Catering B", "Cleaning B", "Decorations B", "Entertainment B", "Furniture B", "Invoice B"),
            (3, "Birthday Party", "Fun", "2024-07-10", "15:00", 4, "Venue C", "Client C", ["Guest 5", "Guest 6"],
             "Catering C", "Cleaning C", "Decorations C", "Entertainment C", "Furniture C", "Invoice C"),
        ]

        for data in event_data:
            event = Event(*data)
            self.events.append(event)

    def add_event(self):
        event_id = int(input("Enter event ID: "))
        type = input("Enter event type: ")
        theme = input("Enter event theme: ")
        date = input("Enter event date (YYYY-MM-DD): ")
        time = input("Enter event time (HH:MM): ")
        duration = int(input("Enter event duration (hours): "))
        venue = input("Enter event venue: ")
        client = input("Enter client name: ")
        guest_list = input("Enter guest list (comma-separated): ").split(',')
        catering_company = input("Enter catering company: ")
        cleaning_company = input("Enter cleaning company: ")
        decorations_company = input("Enter decorations company: ")
        entertainment_company = input("Enter entertainment company: ")
        furniture_company = input("Enter furniture company: ")
        invoice = input("Enter invoice details: ")

        event = Event(event_id, type, theme, date, time, duration, venue, client, guest_list, catering_company,
                      cleaning_company, decorations_company, entertainment_company, furniture_company, invoice)
        self.events.append(event)

        print("Event added successfully!")

    def delete_event(self):
        event_id = int(input("Enter event ID to delete: "))
        for event in self.events:
            if event.get_event_id() == event_id:
                self.events.remove(event)
                print("Event deleted successfully!")
                return
        print("Event not found.")

    def modify_event(self):
        event_id = int(input("Enter event ID to modify: "))
        for event in self.events:
            if event.get_event_id() == event_id:
                print("Modify Event:")
                type = input(f"Enter new type (current: {event.get_type()}): ")
                theme = input(f"Enter new theme (current: {event.get_theme()}): ")
                date = input(f"Enter new date (YYYY-MM-DD) (current: {event.get_date()}): ")
                time = input(f"Enter new time (HH:MM) (current: {event.get_time()}): ")
                duration = int(input(f"Enter new duration (hours) (current: {event.get_duration()}): "))
                venue = input(f"Enter new venue (current: {event.get_venue()}): ")
                client = input(f"Enter new client (current: {event.get_client()}): ")
                guest_list = input(f"Enter new guest list (comma-separated) (current: {event.get_guest_list()}): ").split(',')
                catering_company = input(f"Enter new catering company (current: {event.get_catering_company()}): ")
                cleaning_company = input(f"Enter new cleaning company (current: {event.get_cleaning_company()}): ")
                decorations_company = input(f"Enter new decorations company (current: {event.get_decorations_company()}): ")
                entertainment_company = input(f"Enter new entertainment company (current: {event.get_entertainment_company()}): ")
                furniture_company = input(f"Enter new furniture company (current: {event.get_furniture_company()}): ")
                invoice = input(f"Enter new invoice details (current: {event.get_invoice()}): ")

                event.set_type(type)
                event.set_theme(theme)
                event.set_date(date)
                event.set_time(time)
                event.set_duration(duration)
                event.set_venue(venue)
                event.set_client(client)
                event.set_guest_list(guest_list)
                event.set_catering_company(catering_company)
                event.set_cleaning_company(cleaning_company)
                event.set_decorations_company(decorations_company)
                event.set_entertainment_company(entertainment_company)
                event.set_furniture_company(furniture_company)
                event.set_invoice(invoice)

                print("Event modified successfully!")
                return
        print("Event not found.")

    def display_event(self):
        event_id = int(input("Enter event ID to display: "))
        for event in self.events:
            if event.get_event_id() == event_id:
                print("Event Details:")
                print(f"Event ID: {event.get_event_id()}")
                print(f"Type: {event.get_type()}")
                print(f"Theme: {event.get_theme()}")
                print(f"Date: {event.get_date()}")
                print(f"Time: {event.get_time()}")
                print(f"Duration: {event.get_duration()}")
                print(f"Venue: {event.get_venue()}")
                print(f"Client: {event.get_client()}")
                print(f"Guest List: {event.get_guest_list()}")
                print(f"Catering Company: {event.get_catering_company()}")
                print(f"Cleaning Company: {event.get_cleaning_company()}")
                print(f"Decorations Company: {event.get_decorations_company()}")
                print(f"Entertainment Company: {event.get_entertainment_company()}")
                print(f"Furniture Company: {event.get_furniture_company()}")
                print(f"Invoice: {event.get_invoice()}")
                return
        print("Event not found.")

# Create the Tkinter window and pass it to the ManagementApp class
root = tk.Tk()
app = ManagementApp(root)
root.mainloop()  # Start the Tkinter event loop