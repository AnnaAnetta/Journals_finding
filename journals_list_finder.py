import pandas as pd
import matplotlib.pyplot as plt
dataframe1 = pd.read_excel('journals-list2.xlsx')

def find_journals():

  discipline=input("please input the discipline name: ")
  while discipline not in dataframe1:
    print("this discipline doesn't exist, please try again")
    discipline=input("please input the discipline name: ")
  
  number_of_points=int(input("please input the number of points: "))
  return find_journals_inner(number_of_points, discipline)
  
def find_journals_inner(number_of_points, discipline):
  names_of_journals=[]
  points=[]
  for index, row in dataframe1.iterrows():
  
    if row["Punkty"] >= number_of_points and row[discipline] == "x":
      names_of_journals.append(row["Tytuł 1"])
      points.append(row["Punkty"])

  return [(x,y) for y, x in sorted(zip(points, names_of_journals), reverse=True)]

print(find_journals())

input("press Enter to continue")

def graph_of_points():
  dataframe1.Punkty.value_counts().sort_index().plot(kind="bar")
  plt.title("Journals' points")
  plt.xlabel("Points")
  plt.ylabel("Frequency")
  plt.show()

graph_of_points ()

def test():
  x=find_journals_inner(0,"ekonomia i finanse")
  if len(x)==6:
    print("yes!!!")
  else:
    print("sorry")

test ()