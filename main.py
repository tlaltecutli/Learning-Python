import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def readdata():
    data = pd.read_csv('Iris.csv')
    data.drop('Id',axis=1,inplace=True)
    print(data.head())
    # Plot the training points
    # Setting the figure size and resolution
    fig1 = plt.figure(figsize=(10, 6), dpi=300)
    fig1 = sns.FacetGrid(data, hue = 'Species',
                         size = 5).map(plt.scatter,
                                       'SepalLengthCm',
                                       'SepalWidthCm').add_legend()
    plt.show() # show figure
    
    fig2 = plt.figure(figsize=(10, 6), dpi=300)
    fig2 = sns.boxplot(x = 'Species',
                       y ='PetalLengthCm',
                       data = data,order = ['Iris-virginica',
                                           'Iris-versicolor',
                                           'Iris-setosa'],
                       linewidth = 2.5,
                       orient = 'v',
                       dodge = False)
    plt.show() # show figure                  
    
    fig3 = plt.figure(figsize = (10, 6), dpi = 300)
    fig3 = sns.pairplot(data, hue = 'Species')
    plt.show() # show figure

def main():
    #print("Hello World!")  # This line is used to debug the code
    readdata()

if __name__ == "__main__":
    main()
