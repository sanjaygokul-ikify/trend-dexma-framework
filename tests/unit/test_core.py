import unittest
from unittest.mock import Mock
from packages.core.dexma_engine import DexmaEngine, DexmaAgent, DexmaService

class TestDexmaEngine(unittest.TestCase):
    def test_register_agent(self):
        dexma_engine = DexmaEngine()
        agent = DexmaAgent("test_agent")
        dexma_engine.register_agent(agent)
        self.assertIn("test_agent", dexma_engine.agents)

    def test_register_service(self):
        dexma_engine = DexmaEngine()
        service = DexmaService("test_service")
        dexma_engine.register_service(service)
        self.assertIn("test_service", dexma_engine.services)
