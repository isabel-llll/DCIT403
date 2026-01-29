import spade
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
import random
import datetime
import asyncio  


environment = {
    "area1": {"flood": 0, "fire": 0, "earthquake": 0},
    "area2": {"flood": 0, "fire": 0, "earthquake": 0},
}


class SensorAgent(Agent):
    class MonitorBehaviour(CyclicBehaviour):
        async def run(self):
            
            for area, disasters in environment.items():
                for disaster_type in disasters:
                    
                    severity = random.randint(0, 10)
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    
                    print(f"[{timestamp}] {area} - {disaster_type} severity: {severity}")
            
            
            await asyncio.sleep(5)

    async def setup(self):
        print("SensorAgent starting...")
        
        b = self.MonitorBehaviour()
        self.add_behaviour(b)



async def main():
    
    agent = SensorAgent(
        "sensor.1@xmpp.jp",  
        "Izzy0503"       
    )

    
    await agent.start()
    await spade.wait_until_finished(agent)


if __name__ == "__main__":
    spade.run(main())
