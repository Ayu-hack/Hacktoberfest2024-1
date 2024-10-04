#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Image classification using mnist dataset
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

def load_and_preprocess():
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()

    train_images = tf.image.grayscale_to_rgb(tf.expand_dims(train_images, axis=-1))
    test_images = tf.image.grayscale_to_rgb(tf.expand_dims(test_images, axis=-1))

    train_images = tf.image.resize(train_images, (96, 96))
    test_images = tf.image.resize(test_images, (96, 96))

    train_images = train_images / 255.0 
    test_images = test_images / 255.0

    train_labels = to_categorical(train_labels, 10)
    test_labels = to_categorical(test_labels, 10)

    return train_images, train_labels, test_images, test_labels

def build_model():
    base_model = MobileNetV2(input_shape=(96, 96, 3), include_top=False, weights='imagenet')
    base_model.trainable = False  

    model = models.Sequential([
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.5), 
        layers.Dense(10, activation='softmax') 
    ])

    model.compile(optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'])
    return model

def train_model(model, train_images, train_labels, test_images, test_labels):
    history = model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_data=(test_images, test_labels))
    return history

if __name__=="__main__":
    train_images, train_labels, test_images, test_labels = load_and_preprocess()
    model = build_model()
    history = train_model(model, train_images, train_labels, test_images, test_labels)
    test_loss, test_acc = model.evaluate(test_images, test_labels)
    print(f"Test accuracy: {test_acc}")


# In[ ]:




