import spade
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour


class HelloAgent(Agent):
    class HelloBehaviour(OneShotBehaviour):
        async def run(self):
            print("Hello! I am a SPADE agent running in GitHub Codespaces.")
            await self.agent.stop()

    async def setup(self):
        print("Agent starting...")
        self.add_behaviour(self.HelloBehaviour())


async def main():
    
    agent = HelloAgent(
        "dcit403@xmpp.jp",  
        "Izzy0503"            
    )

    await agent.start()
    await spade.wait_until_finished(agent)


if __name__ == "__main__":
    spade.run(main())