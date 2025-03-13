from crewai import Crew
from agents import planner, writer, editor
from tasks import plan, write, edit

crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    verbose=2
)