# -*- coding: utf-8 -*-
"""Manager class

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15NYLWC6PHaFuMmxbYXEzb-10x2-Cgegn
"""

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