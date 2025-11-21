#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 16:18:17 2025

@author: vaish
"""

# crew_manager.py
from crewai import Crew

class CrewManager:
    """Initializes and runs the CrewAI team"""

    def __init__(self, agents, tasks):
        self.agents = agents
        self.tasks = tasks

    def run(self):
        crew = Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=False
        )
        return crew.kickoff()
