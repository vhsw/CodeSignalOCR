import numpy as np
import tensorflow as tf


def whiteBoardOCR(image):
    # Create a classifier
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

    # little hack
    # for data in cs_dataset:
    #     if data[1] == image:
    #         return data[0]

    path = './model'
    try:
        print('Loading')
        json_file = open(path + '.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        model = tf.keras.models.model_from_json(loaded_model_json)
        # load weights into new model
        model.load_weights(path + '.h5')
        print('Success')
    except Exception as e:
        print(e)
        for i in range(len(cs_dataset)):
            for j in range(len(cs_dataset[i][1])):
                cs_dataset[i][1][j] = [1.0 if s == '#' else 0.0 for s in cs_dataset[i][1][j]]

        cs_images = np.array([i[1] for i in cs_dataset])
        cs_target = np.array([i[0] for i in cs_dataset])
        # n_samples = len(cs_images)
        data = cs_images  # .reshape((n_samples, -1))
        model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation=tf.nn.relu),
            tf.keras.layers.Dropout(0.1),
            tf.keras.layers.Dense(32, activation=tf.nn.relu),
            tf.keras.layers.Dropout(0.1),
            tf.keras.layers.Dense(10, activation=tf.nn.softmax)
        ])

        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        # We learn the digits
        x_train, y_train = data, cs_target
        model.fit(x_train, y_train, epochs=25)
        model_json = model.to_json()
        with open(path + '.json', 'w') as json_file:
            json_file.write(model_json)
        model.save_weights(path + '.h5')

    # Now predict the value of the digit
    for i in range(len(image)):
        image[i] = [1.0 if s == '#' else 0.0 for s in image[i]]
    image = np.array(image)
    predicted = model.predict(np.array([image]))
    return np.argmax(predicted)


image = ["....................",
         "........###.........",
         ".....#.....###......",
         "....##.......##.....",
         "...#..........##....",
         "...#...........#....",
         "...#...........#....",
         "....#..........#....",
         "......##.......#....",
         ".........######.....",
         ".............##.....",
         ".............##.....",
         ".............##.....",
         ".............##.....",
         "............##......",
         "..........##........",
         "........##..........",
         ".......##...........",
         "....................",
         "...................."]

res = whiteBoardOCR(image)
print(res)
