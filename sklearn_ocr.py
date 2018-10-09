# sklearn based, this model not really working
# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>
# License: BSD 3 clause

from random import randint

# Standard scientific Python imports
import matplotlib.pyplot as plt
import numpy as np
# The digits dataset
# digits = datasets.load_digits()
from scipy.ndimage.filters import gaussian_filter
# Import datasets, classifiers and performance metrics
from sklearn import svm, metrics


def whiteBoardOCR(image):
    cs_dataset = [[2, ["....................",
                       "........###.........",
                       ".....####.####......",
                       "....##.......##.....",
                       "...##.........##....",
                       "...#...........#....",
                       "...............##...",
                       "................#...",
                       "...............##...",
                       "...............#....",
                       "..............##....",
                       "............##......",
                       "...........##.......",
                       ".........##.........",
                       "..########..........",
                       "..#..#####.......##.",
                       "..####....########..",
                       "..##................",
                       "....................",
                       "...................."]],
                  [4, ["....................",
                       "....................",
                       ".........#..........",
                       "........##..........",
                       ".......#............",
                       "......##............",
                       "......#.............",
                       ".....##.............",
                       "....##..............",
                       "....#...............",
                       "...##.....#.........",
                       "..##......#.........",
                       "..#.......#.........",
                       ".##############.....",
                       "..........#.........",
                       ".........##.........",
                       ".........#..........",
                       ".........#..........",
                       "....................",
                       "...................."]],
                  [5, ["....................",
                       "....................",
                       "..............##....",
                       ".....#########......",
                       ".....#..............",
                       ".....#..............",
                       "....#...............",
                       "....#...............",
                       "....#...............",
                       "....########........",
                       "............##......",
                       "..............#.....",
                       "..............##....",
                       "...............#....",
                       "..............#.....",
                       "....#.......##......",
                       "....#####.##........",
                       "....................",
                       "....................",
                       "...................."]],
                  [7, ["....................",
                       "....................",
                       "....................",
                       "...###############..",
                       "..##............##..",
                       "...............##...",
                       "...............#....",
                       "..............#.....",
                       ".............##.....",
                       ".............#......",
                       "............##......",
                       "............#.......",
                       "........#########...",
                       "........#..#........",
                       "..........##........",
                       "..........#.........",
                       ".........#..........",
                       "........##..........",
                       "........#...........",
                       ".......##..........."]],
                  [9, ["....................",
                       "....................",
                       ".......####.........",
                       ".....##...###.......",
                       "....#.......#.......",
                       "....#.......##......",
                       "....#........#......",
                       "....#........#......",
                       "....#......##.......",
                       ".....########.......",
                       "............#.......",
                       "...........##.......",
                       "...........#........",
                       "..........##........",
                       "..........#.........",
                       ".........##.........",
                       ".........#..........",
                       "........##..........",
                       ".......##...........",
                       "...................."]],
                  [5, ["....................",
                       "....................",
                       "..........#########.",
                       ".....#####..........",
                       "....##..............",
                       "...##...............",
                       "...#................",
                       "..##................",
                       "..#.................",
                       ".########...........",
                       ".#.......####.......",
                       ".............##.....",
                       "..............##....",
                       "...............#....",
                       "...............#....",
                       "...............#....",
                       "...#..........##....",
                       "...###.......##.....",
                       ".....#########......",
                       "...................."]],
                  [8, ["....................",
                       "....................",
                       "........###.........",
                       "......###.####......",
                       ".....##......#......",
                       ".....#.......#......",
                       "....##.......#......",
                       "....#........#......",
                       "....##......#.......",
                       ".....#......#.......",
                       "......######........",
                       "..........##........",
                       ".......###..##......",
                       "......#.......#.....",
                       ".....#.........#....",
                       ".....#.........#....",
                       "....#..........#....",
                       "....##........##....",
                       "......###....#......",
                       "..........###......."]],
                  [3, ["....................",
                       "......#####.........",
                       ".....#....##........",
                       "...........##.......",
                       "............#.......",
                       "............#.......",
                       "............#.......",
                       "...........##.......",
                       ".........##.........",
                       "........##..........",
                       "..........##........",
                       "...........#........",
                       "...........##.......",
                       "............#.......",
                       "..#.........#.......",
                       "..#........##.......",
                       "..##.......#........",
                       "...##....##.........",
                       "....#####...........",
                       "...................."]],
                  [1, ["....................",
                       "....................",
                       ".........#..........",
                       ".........#..........",
                       ".........#..........",
                       ".........#..........",
                       ".........#..........",
                       ".........#..........",
                       "........#...........",
                       "........#...........",
                       "........#...........",
                       ".......#............",
                       ".......#............",
                       ".......#............",
                       ".......#............",
                       ".......#............",
                       "......#.............",
                       "......#.............",
                       "......#.............",
                       "...................."]],
                  [4, ["....................",
                       ".........#..........",
                       ".........#..........",
                       "........#...........",
                       ".......##...........",
                       ".......#............",
                       "......##............",
                       "......#.............",
                       ".....##.............",
                       ".....#..............",
                       "....##......#.......",
                       "...##.......#.......",
                       "...#........#.......",
                       "...#........#.......",
                       "..###############...",
                       "............#.......",
                       "............#.......",
                       "............#.......",
                       "............#.......",
                       "...................."]],
                  [5, ["....................",
                       "....................",
                       ".......############.",
                       ".......#............",
                       "......##............",
                       "......#.............",
                       "......#.............",
                       "......#.............",
                       "......######........",
                       "............##......",
                       ".............##.....",
                       "..............#.....",
                       "..............##....",
                       "...............#....",
                       "..............#.....",
                       "...##.........#.....",
                       ".....###..####......",
                       ".......####.........",
                       "....................",
                       "...................."]],
                  [0, ["....................",
                       "....................",
                       "......######........",
                       ".....#.....####.....",
                       ".....#........##....",
                       ".....#.........#....",
                       "....##..........#...",
                       "....#...........#...",
                       "....#...........#...",
                       "....#...........#...",
                       "....#...........#...",
                       "....#...........#...",
                       "....#...........#...",
                       "....#...........#...",
                       "....#..........##...",
                       "....##.........#....",
                       ".....##.......##....",
                       "......###....#......",
                       "........#####.......",
                       "...................."]],
                  [6, ["....................",
                       "....................",
                       "..........##........",
                       "........###.........",
                       "........#...........",
                       ".......#............",
                       "......##............",
                       "......#.............",
                       "......#.............",
                       "......#.............",
                       "......#...###.......",
                       "......#.###.####....",
                       "......###......#....",
                       ".......#.......#....",
                       ".......##......#....",
                       "........########....",
                       "....................",
                       "....................",
                       "....................",
                       "...................."]],
                  [4, ["....................",
                       "....................",
                       "........#...........",
                       ".......#............",
                       "......##............",
                       "......#.............",
                       ".....#..............",
                       "....##..............",
                       "....#........#......",
                       "...##........#......",
                       "...#.........#......",
                       "...#.........#......",
                       "..##.........#......",
                       ".##..........#......",
                       "..#########.##..#...",
                       "..........#######...",
                       "............#.......",
                       "............#.......",
                       "............##......",
                       ".............#......"]],
                  [9, ["....................",
                       "....................",
                       ".....#######........",
                       "....#......##.......",
                       "....#.......#.......",
                       "....#.......#.......",
                       "....#......##.......",
                       "....#.....###.......",
                       "....######..#.......",
                       "............#.......",
                       "............#.......",
                       "...........#........",
                       "...........#........",
                       "...........#........",
                       "...........#........",
                       "...........#........",
                       "...........#........",
                       "..........##........",
                       "....................",
                       "...................."]],
                  [2, ["....................",
                       "....................",
                       ".......####.........",
                       ".....##....##.......",
                       "....#........##.....",
                       "..............##....",
                       "...............#....",
                       "...............#....",
                       "..............#.....",
                       ".............##.....",
                       ".............#......",
                       "............#.......",
                       "............#.......",
                       "...........#........",
                       ".........##.........",
                       ".........#..........",
                       ".......##...........",
                       ".....##.............",
                       ".....############...",
                       "...................."]],
                  [3, ["....................",
                       "....................",
                       "..........####......",
                       ".......####..#......",
                       "....###.....#.......",
                       "...........##.......",
                       "..........##........",
                       "..........#.........",
                       ".........#..........",
                       "........#######.....",
                       "..............##....",
                       "...............#....",
                       "...............#....",
                       "..............##....",
                       ".............##.....",
                       "...........###......",
                       "......#####.........",
                       "....##..............",
                       "....................",
                       "...................."]],
                  [7, ["....................",
                       "....................",
                       "....############....",
                       "..............##....",
                       ".............##.....",
                       "............##......",
                       "............#.......",
                       "............#.......",
                       "...........##.......",
                       "...........#........",
                       "...........#........",
                       "..........#.........",
                       "..........#.........",
                       "..........#.........",
                       ".........##.........",
                       ".........#..........",
                       "........##..........",
                       "........#...........",
                       "........#...........",
                       "...................."]],
                  [0, ["....................",
                       "........###.........",
                       "......##...##.......",
                       ".....#.......#......",
                       "....#.........#.....",
                       "....#.........#.....",
                       "...#...........#....",
                       "...#...........#....",
                       "...#...........#....",
                       "..#.............#...",
                       "..#.............#...",
                       "..#.............#...",
                       "...#...........#....",
                       "...#...........#....",
                       "...#...........#....",
                       "....#.........#.....",
                       "....#.........#.....",
                       ".....#.......#......",
                       "......##...##.......",
                       "........###........."]],

                  [1, ["....................",
                       "..........#.........",
                       ".........##.........",
                       "..........#.........",
                       "..........#.........",
                       "..........#.........",
                       "..........#.........",
                       "..........#.........",
                       "..........#.........",
                       "..........#.........",
                       "..........#.........",
                       "..........#.........",
                       "..........#.........",
                       "..........#.........",
                       "..........#.........",
                       "..........#.........",
                       "..........#.........",
                       "..........#.........",
                       "........#####.......",
                       "...................."]],

                  [2, ["....................",
                       ".......#####........",
                       ".....##.....##......",
                       "....#.........#.....",
                       "...#...........#....",
                       "...#...........#....",
                       "................#...",
                       "................#...",
                       "................#...",
                       "................#...",
                       "...............#....",
                       "...............#....",
                       "..............#.....",
                       "............##......",
                       ".........###........",
                       ".......##...........",
                       ".....##.............",
                       "....#...............",
                       "...#................",
                       "...##############..."]],

                  [3, ["....................",
                       "....############....",
                       "...#............#...",
                       "................#...",
                       "...............#....",
                       "..............#.....",
                       ".............#......",
                       "............#.......",
                       "...........#........",
                       "..........#.........",
                       ".........###........",
                       "............##......",
                       "..............#.....",
                       "...............#....",
                       "................#...",
                       "................#...",
                       "................#...",
                       "....#..........#....",
                       ".....##......##.....",
                       ".......######......."]],

                  [4, ["....................",
                       ".........#..........",
                       ".........#..........",
                       "........#...........",
                       ".......#............",
                       ".......#............",
                       "......#.............",
                       ".....#..............",
                       ".....#......#.......",
                       "....#.......#.......",
                       "...#........#.......",
                       "...#........#.......",
                       "..##############....",
                       "............#.......",
                       "............#.......",
                       "............#.......",
                       "............#.......",
                       "............#.......",
                       "............#.......",
                       "...................."]],
                  [5, ["................#...",
                       ".....###########....",
                       "....#...............",
                       "....#...............",
                       "...#................",
                       "...#................",
                       "..#.................",
                       "..#.................",
                       "..######............",
                       "........#####.......",
                       ".............##.....",
                       "...............#....",
                       "................#...",
                       "................#...",
                       "................#...",
                       "................#...",
                       "...............#....",
                       "...............#....",
                       "....#.........#.....",
                       ".....#########......"]],

                  [6, ["....................",
                       "............##......",
                       "..........##........",
                       ".........#..........",
                       "........#...........",
                       ".......#............",
                       "......#.............",
                       ".....#..............",
                       ".....#..............",
                       "....#.....##........",
                       "....#...##..##......",
                       "...#...#......#.....",
                       "...#..#.......#.....",
                       "...#.#.........#....",
                       "...#.#.........#....",
                       "....#..........#....",
                       "....#..........#....",
                       ".....#........#.....",
                       "......##....##......",
                       "........####........"]],

                  [7, ["....................",
                       "...##############...",
                       "..#..............#..",
                       ".................#..",
                       "................#...",
                       "...............#....",
                       "..............#.....",
                       ".............#......",
                       "............#.......",
                       "............#.......",
                       ".......########.....",
                       "...........#........",
                       "..........#.........",
                       "..........#.........",
                       ".........#..........",
                       ".........#..........",
                       "........#...........",
                       "........#...........",
                       "........#...........",
                       "........#..........."]],

                  [8, ["....................",
                       "........###.........",
                       "......##...##.......",
                       ".....#.......#......",
                       "....#.........#.....",
                       "....#.........#.....",
                       "....#.........#.....",
                       ".....#.......#......",
                       "......#.....#.......",
                       ".......#####........",
                       ".....##.....##......",
                       "....#.........#.....",
                       "...#...........#....",
                       "...#...........#....",
                       "..#.............#...",
                       "..#.............#...",
                       "..#.............#...",
                       "...#...........#....",
                       "....##.......##.....",
                       "......#######......."]],

                  [9, ["....................",
                       ".......#####........",
                       ".....##.....##......",
                       "....#.........#.....",
                       "....#.........#.....",
                       "...#...........#....",
                       "...#...........#....",
                       "...#...........#....",
                       "....#.........#.....",
                       "....#.........#.....",
                       ".....##.....##......",
                       ".......#####.#......",
                       ".............#......",
                       ".............#......",
                       "............#.......",
                       "............#.......",
                       "............#.......",
                       "...........#........",
                       "...........#........",
                       "...........#........"]]
                  ]
    for i in range(len(cs_dataset)):
        for j in range(len(cs_dataset[i][1])):
            cs_dataset[i][1][j] = [15.0 if s == '#' else 0.0 for s in cs_dataset[i][1][j]]

    for i in range(len(cs_dataset)):
        for _ in range(10):
            val, data = cs_dataset[i]
            tmp_arr = []
            for line in data:
                tmp_line = []
                for dig in line:
                    if dig > 0:
                        new_dig = 15 * (randint(0, 100) > 20)
                    else:
                        new_dig = 0  # 15 * (randint(0, 100) < 10)
                    tmp_line.append(new_dig)
                tmp_arr.append(tmp_line)
            cs_dataset.append([val, tmp_arr])

    cs_images = np.array([gaussian_filter(i[1], sigma=1.5) for i in cs_dataset])
    cs_target = np.array([i[0] for i in cs_dataset])

    # The data that we are interested in is made of 8x8 images of digits, let's
    # have a look at the first 4 images, stored in the `images` attribute of the
    # dataset.  If we were working from image files, we could load them using
    # matplotlib.pyplot.imread.  Note that each image must have the same size. For these
    # images, we know which digit they represent: it is given in the 'target' of
    # the dataset.
    images_and_labels = list(zip(cs_images, cs_target))
    for index, (image, label) in enumerate(images_and_labels[:8]):
        plt.subplot(2, 8, index + 1)
        plt.axis('off')
        plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
        plt.title('%i' % label)

    # To apply a classifier on this data, we need to flatten the image, to
    # turn the data in a (samples, feature) matrix:
    n_samples = len(cs_images)
    data = cs_images.reshape((n_samples, -1))

    # Create a classifier: a support vector classifier
    classifier = svm.SVC(gamma='scale')

    # We learn the digits on the first half of the digits
    classifier.fit(data[:n_samples // 2], cs_target[:n_samples // 2])

    # Now predict the value of the digit on the second half:
    expected = cs_target[n_samples // 2:]
    predicted = classifier.predict(data[n_samples // 2:])

    print("Classification report for classifier %s:\n%s\n"
          % (classifier, metrics.classification_report(expected, predicted)))
    print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))

    images_and_predictions = list(zip(cs_images[n_samples // 2], predicted))
    for index, (image, prediction) in enumerate(images_and_predictions[:8]):
        plt.subplot(2, 8, index + 9)
        plt.axis('off')
        plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
        plt.title('%i' % prediction)

    plt.show()

    # Now predict the value of the digit

    for i in range(len(image)):
        image[i] = [15.0 if s == '#' else 0.0 for s in image[i]]
    image = np.array(gaussian_filter(image, sigma=1.5))
    image = image.flatten()
    predicted = classifier.predict([image])
    return predicted[0]


image = ["....................",
         "........###.........",
         ".....#########......",
         "....##.......##.....",
         "...#..........##....",
         "...............#....",
         "...............##...",
         "................#...",
         "...............##...",
         "...............#....",
         "..............##....",
         "............##......",
         "...........##.......",
         ".........##.........",
         "......####..........",
         "..#..#####.......##.",
         "..####....########..",
         "....................",
         "....................",
         "...................."]

res = whiteBoardOCR(image)
print(res)