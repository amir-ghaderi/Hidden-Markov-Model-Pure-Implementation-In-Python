#Forward Search
#Amir Ghaderi 500794236
import pandas as pd
import itertools 

print("Transition Matrix")
df = {"Rainy" : [0.6,0.2],"Sunny":[0.4,0.8]}
transition_matrix = pd.DataFrame(df, index=["Rainy","Sunny"])
print(transition_matrix)
print("\n")

print("Emission Matrix")
dff = {"Happy" :[0.4,0.9], "Grumpy" : [0.6,0.1]}
emission_matrix = pd.DataFrame(dff, index =["Rainy","Sunny"])
print(emission_matrix)
print("\n")

print("Initial Distributions")
rainy = 0.5
sunny = 0.5
initial_distributions=[rainy,sunny]
print("P(Rain) = 0.5")
print("P(Sunny) = 0.5")
print("\n")

#Forward Algorithm

def forward(transition,emission,initial,observation_vector):
    alphas = get_initial_alphas(initial[0],initial[1],observation_vector)
    a1 = alphas[0]
    a2 = alphas[1]
    observation_vector = observation_vector[1:len(observation_vector)]
    for i in observation_vector:
        a = a1*transition.loc["Rainy","Rainy"]*emission.loc["Rainy",i]
        b = a2*transition.loc["Sunny","Rainy"]*emission.loc["Rainy",i]
        c = a1*transition.loc["Rainy","Sunny"]*emission.loc["Sunny",i]
        d = a2*transition.loc["Sunny","Sunny"]*emission.loc["Sunny",i]
        a1 = a+b
        a2 = c+d
    return(a1+a2)    

def get_initial_alphas(rain,sun,observation_vector):
    i = observation_vector[0]
    a1 = rain*emission_matrix.loc["Rainy",i]
    a2 = sun*emission_matrix.loc["Sunny",i]
    return(round(a1,5),round(a2,5))
                      

#Exhaustive Search

def exhaustive(transition,emission,initial,observation_vector):
    observation = len(observation_vector)
    combinations = list(itertools.product("SR",repeat=observation))
    total= 0
    for i in combinations:
        sub_total=0.5
        for j in range(1,observation):
            if i[j-1] == "R":
                if i[j] == "R":
                    sub_total =  sub_total * transition.loc["Rainy","Rainy"]
                if i[j] == "S":
                    sub_total =  sub_total * transition.loc["Rainy","Sunny"]
            if i[j-1] == "S":
                if i[j] == "R":
                    sub_total =  sub_total * transition.loc["Sunny","Rainy"]
                if i[j] == "S":
                    sub_total =  sub_total * transition.loc["Sunny","Sunny"]
        for j in range(observation):
            if i[j] == "R":
                if observation_vector[j] == "Happy":
                    sub_total =  sub_total * emission.loc["Rainy","Happy"]
                if observation_vector[j] == "Grumpy":
                    sub_total =  sub_total * emission.loc["Rainy","Grumpy"]
            if i[j] == "S":
                if observation_vector[j] == "Happy":
                    sub_total =  sub_total * emission.loc["Sunny","Happy"]
                if observation_vector[j] == "Grumpy":
                    sub_total =  sub_total * emission.loc["Sunny","Grumpy"]
        
        total = total + sub_total
    return total


print("Queries")
print("Forward Algorithm")
print("Observation Vector = [Happy, Grumpy]")
Final = forward(transition_matrix,emission_matrix,initial_distributions,["Happy", "Grumpy"])                   
print(Final)    
print("Observation Vector = [Happy, Grumpy, Happy]")
Final = forward(transition_matrix,emission_matrix,initial_distributions,["Happy", "Grumpy","Happy"])                   
print(Final)
print("Observation Vector = [Happy, Grumpy, Grumpy, Happy]")
Final = forward(transition_matrix,emission_matrix,initial_distributions,["Happy", "Grumpy","Grumpy","Happy"])                   
print(Final)
print("\n")
print("Exhaustive search")
print("Observation Vector = [Happy, Grumpy]")  
Final2 = exhaustive(transition_matrix,emission_matrix,initial_distributions,["Happy", "Grumpy"])                   
print(Final2)                 
print("Observation Vector = [Happy, Grumpy, Happy]")    
Final2 = exhaustive(transition_matrix,emission_matrix,initial_distributions,["Happy", "Grumpy","Happy"])                   
print(Final2)
print("Observation Vector = [Happy, Grumpy, Grumpy, Happy]")   
Final2 = exhaustive(transition_matrix,emission_matrix,initial_distributions,["Happy", "Grumpy","Grumpy","Happy"])                   
print(Final2)

    
