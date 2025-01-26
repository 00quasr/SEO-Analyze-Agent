from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
import openai  # Import OpenAI
import os  # Import os module for accessing environment variabl
import yaml

from crewai_tools import ScrapeWebsiteTool  # Import the tool

load_dotenv()

# Uncomment the following line to use an example of a custom tool
# from ai_latest_development.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class SEOAnalyseCrew():
	"""SEOAnalyseCrew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	def __init__(self, website_url: str):
		self.website_url = website_url
		# Load configuration files
		with open(self.agents_config, 'r') as f:
			self.agents_config = yaml.safe_load(f)
		with open(self.tasks_config, 'r') as f:
			self.tasks_config = yaml.safe_load(f)

	# Configure OpenAI LLM
	openai_llm = LLM(
		model='gpt-4o',  # Use the model specified in your .env
		api_key=os.getenv('OPENAI_API_KEY'),  # Use the API key from .env
	)

	@agent
	def scraper_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['scraper_agent'],
			tools=[ScrapeWebsiteTool(website_url=self.website_url)],
			verbose=True,
			llm=self.openai_llm  
		)

	@agent
	def analyse_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['analyse_agent'],
			verbose=True,
			llm=self.openai_llm  
		)
	
	@agent
	def optimization_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['optimization_agent'],
			verbose=True,
			llm=self.openai_llm  
		)

	@task
	def data_collection_task(self) -> Task:
		task_config = self.tasks_config['data_collection_task']
		return Task(
			description=task_config['description'].format(website_url=self.website_url),
			agent=self.scraper_agent(),
			expected_output=task_config['expected_output']
		)

	@task
	def analysis_task(self) -> Task:
		task_config = self.tasks_config['analysis_task']
		return Task(
			description=task_config['description'],
			agent=self.analyse_agent(),
			expected_output=task_config['expected_output'],
			output_file='report.md'
		)

	@task
	def optimization_task(self) -> Task:
		task_config = self.tasks_config['optimization_task']
		return Task(
			description=task_config['description'],
			agent=self.optimization_agent(),
			expected_output=task_config['expected_output'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the SEOAnalyseCrew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)
