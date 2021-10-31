from collections import deque
from typing import List

"""
Ctci 7.2: 

Imagine you have a call center with three levels of employees: 

    1) respondent
    2) manager
    3) director 
    
Rules:
    - An incoming telephone call must be first allocated to a respondent who is free. 
    - If the respondent can't handle the call, 
        he or she must escalate the call to a manager. 
    - If the manager is not free or not able to handle it, 
        then the call should be escalated to a director. 
        
Question: 
a) Design the classes and data structures for this problem. 
b) Implement a method dispatch_call() which assigns a call to the first available employee.

Clarifying:
    1) #'s of each employee?
        - nonnegative 
        - ASSUME >= 1 of each
            - 1 only director
            - ASSUME that CallCenter is passed in tree of Employees in contstructor

                D
               /  \
              M    M 
                    \
             /\\     R
            R R R
        - ASSUME we don't need worry employee can handle a call or not
            Employee.canHandle(call: Call)
        - ASSUMM
    2) Synchroncity:
        - ASSUME can only handle 1 call at a time

        t ------|-------
                0

        Intuition:
            CallCenter:
                - queue of calls
                    - list - front first indedx; back  last index
                - collection of employees
                    1) 3 separate arrays
                        - 1 Director, Manager, Emplyyes
                    2) tree of Employee + array of Respondents
                - [TODO] CallCenter: 
                - [TODO] constructor:
                    - EmployeeTree, CallQueue
                    - iterate over each call (While)
                        - iterate over List[Respondent]
                            - if employee.can_handle(call)
                                - [TODO] employee.dispatch_call(call)
                            - if not possible, -> get a list of upper level
                - Singleton [TODO]

            Call class:
                - timeLength: how muhc time on the phone
            
            Employee:
                - Props:
                    - superior
                    - canHandle(call: Call)
                Sub classes:
                    - Respondent (sub)
                    - Manager (sub)
                    - Director (sub)

"""


class Call:
    pass


class Employee:
    def __init__(self, superior=None, subordinates=[]):
        self.superior = superior
        self.subordinates = subordinates
        self.is_handle = True

    def can_handle(self, call: Call):
        pass

    def handle_call(self, call):
        pass


class Respondent(Employee):
    def __init__(self, superior: "Manager"):
        super().__init__(superior)


class Manager(Employee):
    def __init__(self, superior, respondents: List[Respondent]):
        super().__init__(superior, respondents)


class Director(Employee):
    def __init__(self, managers: List[Manager]):
        super().__init__(subordinates=managers)


class EmployeeGraph:
    def __init__(self, director):
        self.director = director

    def get_respondents(self):
        """
        Get all respondents via iterative BFS
        """
        # A: init a list of respondents
        respondents = list()
        # B: populate list via managers
        for manager in self.director.subordinates:
            if isinstance(manager, Manager):
                for r in manager.subordinates:
                    if isinstance(r, Respondent):
                        respondents.append(r)
        return respondents


class CallCenter:
    def __init__(self, employees: EmployeeGraph, calls: deque[Call]):
        self.employees = employees
        self.calls = calls

    def dispatch_call(self, call: Call) -> str:
        # exhaustively search for available employes
        respondent_queue = deque(self.employees.get_respondents())
        rq, manager_queue = respondent_queue, []
        # [TODO-Refactor] BFS upwards
        while len(rq) > 0:
            respondent = rq.popleft()
            if respondent.can_handle(call):
                respondent.handle(call)
                return "success!"
            else:
                manager_queue.append(respondent.superior)
        mq = manager_queue
        director = mq[0].superior
        while len(mq) > 0:
            manager = mq.popleft()
            if manager.can_handle(call):
                manager.handle(call)
                return "success!"
        if director.can_handle(call):
            director.handle(call)
            return "success!"
        return "put them on hold for now!"
