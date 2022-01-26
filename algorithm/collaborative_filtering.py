from algorithm.algorithm import Algorithm


class CollaborativeFiltering(Algorithm):
    def __init__(self, data_base):
        super().__init__()
        self.__data_base = data_base
        self.__ranking = {}

    def create_ranking(self):
        ratings = []
        for model in self.__data_base:
            if self.__data_base[model]['rating'] not in ratings:
                ratings.append(self.__data_base[model]['rating'])
        ratings = sorted(ratings, reverse=True)
        for rating in ratings:
            place = ratings.index(rating) + 1
            for model in self.__data_base:
                if self.__data_base[model]['rating'] == rating:
                    if place not in self.__ranking:
                        self.__ranking[place] = []
                    self.__ranking[place].append(model)
        print(self.__ranking)

    def save_ranking_Excel(self, workbook):
        workbook.save_collaborative_ranking(self.__ranking)
