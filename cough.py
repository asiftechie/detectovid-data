def predict(df, media_path, h5):
    """
    Inputs:
    - df: A pandas dataframe of shape (m, ?) containing the input data
    - h5: The best trained model file for this class

    Outputs:
    - A numpy array of shape (m, 1) outputting the predicted probability of
      COVID-19 by this model
    """

    # pre process to delete unneeded columns from the dataframe
    # load the .mp4 files, break into images if needed
    
    model = cough_model(data, media)
    model.load(h5)
    return model.predict()

class cough_model:
    def __init__(self, df, media_path):
      self.df = df
      self.media_path = media_path
      
    def predict():
        return 0.75
      
    def train():
        #h5 = keras save_model to h5
        return
