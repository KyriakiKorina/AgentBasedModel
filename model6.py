''' The following is an agent-based model where each agent has his behavior 
and also the ability to interact with other agents and with the environment. 
All agents can move one step at a time and not move a large number of steps. 
Moving each agents one step at a time, allows agents to interact as they move around. '''


import random
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.backends.backend_tkagg
import operator
import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation 
import requests
import bs4

'''download and print x,y - is initialised with data from the web'''

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)
 
'''the function that takes in two arbitary agents and returns the distance between them'''
def distance_between(agent0, agent1):
    return(((agent0.x - agent1.x)**2) + ((agent0.y - agent1.y)**2))**0.5
        
    
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
environment = []
agents = []
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])   


'''Read txt- Reads environmental data'''
    
f = open ("in.txt")
data = []
for line in f:
    parsed_line = str.split(line,",")
    data_line = []
    for word in parsed_line:
        data_line.append(float(word))
    data.append(data_line)
#print (data)
    
for row in data:
    rowlist = []
    for item in row:
        rowlist.append(item)
    environment.append(rowlist)

''' build agents '''

for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))
    


def update(frame_number):
    fig.clear()  

      
    '''Move the agents - interact with the environment'''

    for j in range(num_of_iterations):
        
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            
            
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    matplotlib.pyplot.imshow(environment)    

'''dislay the model as an animation'''
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
    canvas.show() 
    
'''make a menu associated with the fuction run'''
root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 

'''GUI is ready for events'''
tkinter.mainloop() 

    
    

    

