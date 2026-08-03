import asyncio
from typing import Dict
from .types import DexmaRuntimeConfig
from ..core.engine import DexmaEngine
from ..core.types import DexmaAgent, DexmaService

class DexmaRuntimeExecutor:
    def __init__(self, config: DexmaRuntimeConfig):
        self.config = config
        self.engine = DexmaEngine()
        self.logger = logging.getLogger(__name__)

    async def start(self):
        self.logger.info("Dexma runtime started")
        await self.engine.start()

    async def register_agent(self, agent: DexmaAgent):
        await self.engine.register_agent(agent)

    async def register_service(self, service: DexmaService):
        await self.engine.register_service(service)

    async def discover_services(self, agent_name: str):
        return await self.engine.discover_services(agent_name)

    async def request_service(self, agent_name: str, service_name: str):
        return await self.engine.request_service(agent_name, service_name)

@dataclass
class DexmaRuntimeConfig:
    agents: Dict[str, DexmaAgent]
    services: Dict[str, DexmaService]
