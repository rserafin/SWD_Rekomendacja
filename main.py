from parser_package.data import Data
from algorithm.collaborative_filtering import CollaborativeFiltering
from algorithm.content_based_filtering import ContentBasedFiltering
from saving_data.create_workbook import DataWorkbook

brand_list = ['Samsung', 'Xiaomi', 'POCO', 'Motorola', 'Redmi']
models_name_raw_brand = {'Samsung':
                            ['galaxya52s5gdualsim', 'galaxya53', 'galaxynote20ultra5gdualsim', 'galaxya135g', 'galaxym52', 'galaxyf22', 'galaxym32', 'galaxya22', 'galaxya32', 'galaxya02'],
                         'Xiaomi':
                            ['11i', '11t', '11tpro', '12pro', 'mix4', 'mi11', 'mi11i', 'mi11lite', 'mi11pro', 'mi10pro'],
                         'POCO':
                            ['x2', 'x3', 'x3pro', 'x3gt', 'm2', 'm2pro', 'm3', 'f3', 'f3gt', 'm4pro5g'],
                         'Motorola':
                            ['motoedges30', 'motog2005g', 'motog31', 'motog71', 'motog41', 'motog505g', 'motoe20', 'motog20', 'motog60', 'edges'],
                         'Redmi':
                            ['note11', 'note11t', '10', 'note10t', '9isport', '9power', '9i', 'note95g', 'k30s', '9at']
                         }
data = Data(brand_list, models_name_raw_brand)
data.download_data()
data_base = data.get_all_data()
workbook = DataWorkbook()
workbook.save_data(data_base)

collaborative = CollaborativeFiltering(data_base)
collaborative.create_ranking()
collaborative.save_ranking_Excel(workbook)
workbook.save_file_workbook()


