import matplotlib.pyplot as plt
from math import floor as floor

def plotDatasets(datasets):
    # configure fig
    rows = floor(len(datasets)/2) # if n° of data sets is odd, we will have an extra row with the remaining elements
    cols = floor(len(datasets)/2)
    fig, axes = plt.subplots(nrows=rows, ncols=cols, constrained_layout=True)
    # data set index
    i = 0
    # iterate over the axes
    for r in range(rows):  # row index
        # iterate over the algorithms
        for c in range(cols):  # column index
            # get current axis
            ax = axes[r, c]
            # we will iterate over the columns and if the n° of data sets is odd, some columns for the last row will be empty
            # and an error may raise if trying to access a position that does not exist in the list
            try:
                params, dataset = datasets[i]
                x, y = zip(*dataset)
                ax.plot(x, y, "o", alpha=0.5, )
                text = params['name'] + ", k = " + params["k"]
                ax.set_title(text, size=9)
            except:
                # hide subplot
                ax.axis('off')
            # increment data sets index
            i += 1
    # show
    plt.show()