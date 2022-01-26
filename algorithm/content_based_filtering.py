from algorithm.algorithm import Algorithm


class ContentBasedFiltering(Algorithm):
    def __init__(self, data_base, criteria):
        super().__init__()
        self.__data_base = data_base
        self.__criteria = criteria
        self.__ranking = {}

