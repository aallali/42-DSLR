# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pair_plot.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aallali <hi@allali.me>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/26 12:49:21 by aallali           #+#    #+#              #
#    Updated: 2021/06/26 15:16:29 by aallali          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import seaborn as sns
import matplotlib.pyplot as plt
import sys
from DSLR.utils import read_file

def main():
    if (len(sys.argv) <= 1):
        sys.exit("No name file")
    if (len(sys.argv) >= 3):
        sys.exit("too much file")
    data = read_file(sys.argv[1])
    # after see the pair plot, histogram, scatterplot i decied to move up best hand
    # , arytmencie, care of magic creature and astronomy
    data = data.drop(['Best Hand', 'Care of Magical Creatures', 'Charms', 'Astronomy'], \
                     axis=1)

    sns.pairplot(data, hue="Hogwarts House", height=1, diag_kind='hist')
    plt.show()


if __name__ == "__main__":
    main()
