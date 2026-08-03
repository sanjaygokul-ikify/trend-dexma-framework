import unittest
from packages.core.dexma_engine import DexmaEngine, DexmaAgent, DexmaService

class TestDexmaRuntime(unittest.TestCase):
    def test_start_agent(self):
        dexma_engine = DexmaEngine()
        agent = DexmaAgent("test_agent")
        dexma_engine.register_agent(agent)
        dexma_engine.start_agent(agent)
