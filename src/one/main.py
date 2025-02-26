from crewai.flow.flow import Flow, start, listen
import time

class SimpleFlow(Flow):
    
    @start()
    def function1(self):
        print("Step 1")
        time.sleep(1)
        
    @listen(function1)
    def function2(self):
        print("Step 2")
        time.sleep(1)
        
    @listen(function2)  
    def function3(self):
        print("Step 3")
        time.sleep(1)


def kickoff():
    obj = SimpleFlow()
    obj.kickoff()
    
def plot():
    obj = SimpleFlow()
    obj.plot()
    
    
    