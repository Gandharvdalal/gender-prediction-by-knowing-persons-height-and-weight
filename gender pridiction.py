from sklearn import tree
#[height,weight]
x=[[174,96],[184,87],[185,110],[195,104],[149,61],[189,104],[147,92],[154,111],[174,90],[169,103]]
y=['male','male','female','female','male','male','male','male','male','female']
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)
a=int(input("enter  the height in cm"))
b=int(input("enter the weight in kg"))    
prediction=clf.predict([[a,b]])
print(prediction)
