from packages.core.dexma_engine import DexmaEngine

class Orchestrator:
    def __init__(self, dexma_engine: DexmaEngine):
        self.dexma_engine = dexma_engine

    async def start(self):
        await self.dexma_engine.start()
