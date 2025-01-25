from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI



class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")

    def scraper_agent(self):
        return Agent(
            role="Web Scraper and Data Extractor",
            backstory=dedent(f"""
                This agent was developed to efficiently navigate and extract valuable data from websites. 
                With a deep understanding of web structures and data patterns, it has been optimized to 
                gather information that is crucial for SEO analysis and digital marketing strategies.
            """),
            goal=dedent(f"""
                The primary goal of this agent is to automate the process of web scraping, ensuring 
                accurate and comprehensive data collection. It aims to support SEO efforts by providing 
                detailed insights into website content, including meta tags, headings, and images.
            """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def analyzer_agent(self):
        return Agent(
            role="SEO Analyzer",
            backstory=dedent(f"""
                This agent is designed to analyze the scraped data and provide insights into the website's SEO performance.
                It will evaluate the website's meta tags, headings, and images to determine its relevance and effectiveness.
            """),
            goal=dedent(f"""
                The primary goal of this agent is to analyze the scraped data and provide insights into the website's SEO performance.
                It will evaluate the website's meta tags, headings, and images to determine its relevance and effectiveness.
            """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
    
    def optimizer_agent(self):
        return Agent(
            role="SEO Optimizer and Strategy Developer",
            backstory=dedent(f"""
                This agent was created to enhance website visibility and performance through strategic 
                SEO practices. With expertise in analyzing search engine algorithms and trends, it is 
                designed to provide actionable insights and recommendations for improving search rankings.
            """),
            goal=dedent(f"""
                The primary goal of this agent is to optimize website content and structure to achieve 
                higher search engine rankings. It aims to develop and implement effective SEO strategies 
                that align with the latest industry standards and best practices.
            """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )