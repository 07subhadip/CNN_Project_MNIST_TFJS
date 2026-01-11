import sys
import types
import os
import shutil



import tensorflow as tf
import tensorflowjs as tfjs

def convert_model():
    input_path = 'Subhadip_Hensh_MNIST_CNN.keras'
    output_dir = 'tfjs_model'
    temp_dir = 'temp_tf_saved_model'

    if not os.path.exists(input_path):
        print(f"Error: Model file '{input_path}' not found.")
        return

    print(f"Loading Keras model: {input_path}")
    try:
        model = tf.keras.models.load_model(input_path)
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {e}")
        return


    try:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            
        if hasattr(model, 'export'):
            model.export(temp_dir)
        else:
            tf.saved_model.save(model, temp_dir)
            
        print("Intermediate SavedModel created.")
    except Exception as e:
        print(f"Failed to create intermediate SavedModel: {e}")
        try:
             model.save(temp_dir, save_format='tf')
        except:
             pass
        return

    print("Step 2: Converting SavedModel to TensorFlow.js format...")
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        tfjs.converters.convert_tf_saved_model(temp_dir, output_dir)
        
        print(f"Success! Model saved to '{output_dir}' directory.")
        
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            
    except Exception as e:
        print(f"Conversion error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    convert_model()
