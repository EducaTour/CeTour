import tensorflow as tf

class Prediction():
    def __init__(self, model_path: str, classes: list, target_size: tuple=(224,224)):
        self.model_path = model_path
        self.classes = classes
        self.target_size = target_size

        try:
            self.__loaded_model = tf.keras.models.load_model(self.model_path)
        except Exception as e:
            print(e)
        
        self.__prepared_img = None

    def model_summary(self):
        return self.__loaded_model.summary()
        
    def __preprocess_img(self, img):
        img = tf.io.read_file(img)
        img = tf.io.decode_image(img)
        img = tf.image.resize(img, self.target_size)    
        return img
    
    def predict_class(self, img):
        img = self.__preprocess_img(img)
        pred_prob = self.__loaded_model.predict(tf.expand_dims(img, axis=0))
        pred_cat = pred_prob.argmax(axis=-1)
        pred_class = self.classes[pred_cat[0]]
        confidence_score = pred_prob.max() * 100
        confidence_score = f"{confidence_score:.2f}"
        return pred_class, confidence_score