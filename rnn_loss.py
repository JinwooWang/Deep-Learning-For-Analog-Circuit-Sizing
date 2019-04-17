
import matplotlib.pyplot as plt

def loss_plot():
    lf = open("train_cost.log", "r").readline()
    splited_line = lf.split()
    loss = []
    i = 0
    for item in splited_line:
        if i % 100 == 0:
            loss.append(float(item))
        i += 1
    plt.title("rnn train loss")
    plt.plot(loss, c = "b")
    plt.show()

if __name__ == "__main__":
    loss_plot()
