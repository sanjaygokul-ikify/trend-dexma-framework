import logging
from typing import Dict, List
import asyncio
from .types import DexmaAgent, DexmaService
from .exceptions import DexmaEngineException

class DexmaEngine:
    def __init__(self):
        self.agents: Dict[str, DexmaAgent] = {}
        self.services: Dict[str, DexmaService] = {}
        self.logger = logging.getLogger(__name__)

    async def register_agent(self, agent: DexmaAgent):
        if agent.name in self.agents:
            self.logger.warning(f"Agent {agent.name} already registered")
        else:
            self.agents[agent.name] = agent
            self.logger.info(f"Agent {agent.name} registered")

    async def register_service(self, service: DexmaService):
        if service.name in self.services:
            self.logger.warning(f"Service {service.name} already registered")
        else:
            self.services[service.name] = service
            self.logger.info(f"Service {service.name} registered")

    async def discover_services(self, agent_name: str):
        if agent_name not in self.agents:
            self.logger.error(f"Agent {agent_name} not registered")
            raise DexmaEngineException(f"Agent {agent_name} not registered")
        services = list(self.services.values())
        self.logger.info(f"Services discovered for agent {agent_name}: {services}")
        return services

    async def request_service(self, agent_name: str, service_name: str):
        if agent_name not in self.agents:
            self.logger.error(f"Agent {agent_name} not registered")
            raise DexmaEngineException(f"Agent {agent_name} not registered")
        if service_name not in self.services:
            self.logger.error(f"Service {service_name} not registered")
            raise DexmaEngineException(f"Service {service_name} not registered")
        service = self.services[service_name]
        self.logger.info(f"Service {service_name} requested by agent {agent_name}")
        return service

    async def start(self):
        self.logger.info("Dexma engine started")
        await asyncio.gather(*[self.start_agent(agent) for agent in self.agents.values()])

    async def start_agent(self, agent: DexmaAgent):
        try:
            await agent.start()
            self.logger.info(f"Agent {agent.name} started")
        except Exception as e:
            self.logger.error(f"Error starting agent {agent.name}: {str(e)}")
            raise
