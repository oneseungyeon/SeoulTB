from tensorflow.keras.preprocessing.image import ImageDataGenerator
from DeepResUNet_3 import DeepResUNet
import tensorflow as tf

x_datagen = ImageDataGenerator()
x_generator = x_datagen.flow_from_directory(
    directory='',
    target_size=(512, 512),
    seed=10,
    shuffle=True,
    class_mode=None,
    batch_size=5
)

t_datagen = ImageDataGenerator()
t_generator = t_datagen.flow_from_directory(
    directory='',
    target_size=(512, 512),
    seed=10,
    shuffle=True,
    class_mode=None,
    color_mode="grayscale",
    batch_size=5
)


def create_test_generator(gen_x, gen_t):
    while True:
        for x, t in zip(gen_x, gen_t):
            yield x, t

INPUT_SHAPE = (512, 512, 3)
NUM_CLASSES = 2
initial_learning_rate = 1e-4
end_learning_rate = 1e-7
decay_steps = 100
weight_decay = 0.00001
LR = tf.keras.optimizers.schedules.PolynomialDecay( initial_learning_rate = initial_learning_rate,
    decay_steps=decay_steps, end_learning_rate=end_learning_rate, power=0.9, cycle=False, name=None)
BATCH_SIZE = 5
seed = 10

model = DeepResUNet(input_size=INPUT_SHAPE, lr=LR, num_classes=NUM_CLASSES).build_net()

model.load_weights('')

valid_generator = create_test_generator(x_generator, t_generator)

model.evaluate(valid_generator, steps=20)
