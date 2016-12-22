class DataCollector:
    """
    Class for Data Collection from Historic Game data.
    Handles writing and reading of the feature matrix.
    """
    def __init__(self):
        pass

    def generate_feature_matrix(self):
        """
        Generate the feature matrix from all historic data.
        :return: the feature matrix.
        """
        pass

    def write_feature_matrix(self):
        """
        Writes the feature matrix to a .mat file.
        :return: Boolean flag indicating whether the writing was successful. If
        the data matrix has not been generated yet, it will return False.
        """
        pass

    def retrieve_feature_matrix(self):
        """
        Retrieves the Feature Matrix.
        :return: the Feature Matrix if it has been written and saved yet. None if
        the Matrix has not been saved to a .mat file.
        """
        pass

    def featurize_game(self):
        """
        Featurizes a single game.
        :return: Feature vector of that single game.
        """
        pass
