#tools for the agent use
#tools can be of 2 types: USER DEFINED  and PRE-DEFINED in the tools module

#user defined functions can be used as the tools
def get_weather(city):
  "get the weather of the current week of the city"
  #if you want to use a specific website for the info you can mention the website
total=0
#simple or complex functions can be used as tools as models
def avgarr(array1:int[]):
  for i in range(len(array1)):
    total=(total+array[i])
  return round(total/len(array),2)

#the TOOL RULE:
#the input given to the function is seen as the actual input/TARGET
#the body of the fucntion which can be a set of steps or simply a comment taht suggests the model on what task to perform on the input

#replacing the note of thr tool
weather=ezk.tool(get_weather,"check the rain patterns in the region")
print(weather.note)

#usinf the .run command
#as any AI system maps its inputs as a graph
#the run feature does the same, ut returns the text that the agent is about to see
print(ezk.tool(get_weather).run({"city":"Chennai"}))


#PRE DEFINED TOOLS form the TOOLS module 
from eztraink import tools as ts
#the pre defined tools are as follows
#CALCULATOR
#to introduce the deterministic mathematical approach to places where neccessary sot hat the moddel never guesses a mathematical answer
ts.calculator("2450*0.18)










  
