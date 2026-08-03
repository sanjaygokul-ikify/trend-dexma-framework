import unittest
from packages.core.dexma_engine import DexmaEngine, DexmaAgent, DexmaService
from services.orchestrator import Orchestrator

class TestDexmaPipeline(unittest.TestCase):
    def test_full_pipeline(self):
        dexma_engine = DexmaEngine()
        agent = DexmaAgent("test_agent")
        service = DexmaService("test_service")
        dexma_engine.register_agent(agent)
        dexma_engine.register_service(service)
        orchestrator = Orchestrator(dexma_engine)
        orchestrator.start()
