import sys, os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_learning_curves(fpath, title=None, save_path=None):
    df = pd.read_csv(fpath)
    print('Plotting')
    if title is None:
        title = os.path.basename(fpath)
    if save_path is not None:
        plt.ioff()
        plt.switch_backend('agg')

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    fig.suptitle(title)

    sns.lineplot(x='epoch', y='train_dice', data=df, label="Training", ax=ax1)
    sns.lineplot(x='epoch', y='test_dice', data=df, label="Testing", ax=ax1)
    ax1.set(xlabel='Epochs', ylabel='Dice', title='Dice')

    sns.lineplot(x='epoch', y='train_loss', data=df, label="Training", ax=ax2)
    sns.lineplot(x='epoch', y='test_loss', data=df, label="Testing", ax=ax2)
    ax2.set(xlabel='Epochs', ylabel='Loss', title='Loss')

    sns.lineplot(x='epoch', y='train_volume_error', data=df, label="Training", ax=ax3)
    sns.lineplot(x='epoch', y='test_volume_error', data=df, label="Testing", ax=ax3)
    ax3.set(xlabel='Epochs', ylabel='Volume Error', title='Volume Error')

    fig.tight_layout(rect=[0, 0.03, 1, 0.95])

    if save_path is not None:
        fig.savefig(save_path, dpi='figure', format='png')
        plt.close(fig)
    else:
        plt.show()


if __name__ == '__main__':
    path = sys.argv[1]
    plot_learning_curves(path)
