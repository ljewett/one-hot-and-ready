import os
import numpy as np
import xgboost as xgb
import matplotlib.pyplot as plt
from matplotlib.colors import PowerNorm


class Imager():
    @staticmethod
    def get_directory():
        if os.path.isdir('./images'):
            return './images'
        return '.'

    @staticmethod
    def generate_heatmap(prediction, label):
        output = np.zeros((8, 8), dtype=int)
        for t in zip(prediction, label):
            output[int(t[0]), int(t[1])] += 1

        directory = Imager.get_directory()

        plt.imshow(output[1:, 1:], extent=[1, 7, 7, 1], norm=PowerNorm(gamma=1./4.), interpolation='nearest')
        plt.xlabel('Actual')
        plt.ylabel('Prediction')
        plt.savefig(os.path.join(directory, 'heatmap.png'))

    @staticmethod
    def generate_tree_image(model, tree_num):
        directory = Imager.get_directory()
        path = os.path.join(directory, '{}.png'.format(tree_num))
        xgb.plot_tree(model, num_trees=tree_num, rankdir='LR').figure.savefig(path, format='png', dpi=300)
