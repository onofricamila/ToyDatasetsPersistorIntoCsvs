import matplotlib.pyplot as plt
from math import floor as floor
# set matplotlib backend to Qt5Agg to make figure window maximizer work
import matplotlib
matplotlib.use('Qt5Agg')

def plotDatasets(datasets):
    # configure fig
    rows = floor(len(datasets)/2) # if n° of data sets is odd, the last row will be incomplete
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
                k = params["k"]
                if k == '':
                    # 'k' was not specified
                    k = '---'
                text = params['name'] + ", k = " + k
                ax.set_title(text, size=9)
            except BaseException as e:
                print(e)
                # hide subplot (if not it will be empty)
                ax.axis('off')
            # increment data sets index
            i += 1
    # show
    fig.canvas.manager.window.showMaximized()
    plt.show()