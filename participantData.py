# # Participant Data Part A

# participantNumber = 5
# participantData = []
# registeredParticipants = 0
# outputFile = open('participantData.txt','w')

# while(registeredParticipants < participantNumber):
#     tempPartData = [] # name, country of origin, age
#     name = input('Please enter your name : ')
#     tempPartData.append(name)
#     country = input('Please enter your country of origin : ')
#     tempPartData.append(country)
#     age = int(input('Please enter your age : '))
#     tempPartData.append(age) # [name,country,age]
#     print(tempPartData)
#     participantData.append(tempPartData)
#     print(participantData)
#     # [tempPartData] = [[name,country,age]]
#     registeredParticipants += 1

# for participant in participantData:
#     for data in participant:
#         outputFile.write(str(data))
#         outputFile.write(' ')
#     outputFile.write('\n')    

# outputFile.close()


# # Part B

inputFile = open('participantData.txt','r')

inputList = []

for line in inputFile:
    tempParticipant = line.strip('\n').split()
    # print(tempParticipant)
    inputList.append(tempParticipant)
    # print(inputList)

    # "Max U.S. 21 \n".strip("\n") -> "Max U.S. 21 "
    # "Max U.S. 21 ".split() -> ["Max","U.S.","21"]

age = {}
for part in inputList:
    tempAge = int(part[-1]) #int('21') -> 21
    if tempAge in age:
        age[tempAge] += 1
    else:
        age[tempAge] = 1

print(age)

countries = {}
for part in inputList:
    tempCountries = part[1]
    if tempCountries in countries:
        countries[tempCountries] += 1
    else:
        countries[tempCountries] = 1
print("Countries that attended :",countries)
# inputFile.close()

# # Part C

oldest = 0
youngest = 100
mostOccuringAge = 0
counter = 0

for tempAge in age:
    if tempAge>oldest:
        oldest = tempAge
    if tempAge<youngest:
        youngest = tempAge
    if age[tempAge]>=counter:
        counter = age[tempAge]
        mostOccuringAge = tempAge

print(oldest)
print(youngest)
print("Most occuring age is : ",mostOccuringAge,"with ", counter,"participants")


inputFile.close()


