import pprint
import operator
import json

import numpy as np


from collections import OrderedDict

pp = pprint.PrettyPrinter(indent=4)


departements = [
    '01',
    '02',
    '03',
    '04',
    '05',
    '06',
    '07',
    '08',
    '09',
    '10',
    '11',
    '12',
    '13',
    '14',
    '15',
    '16',
    '17',
    '18',
    '19',
    '2B',
    '2A',
    '21',
    '22',
    '23',
    '24',
    '25',
    '26',
    '27',
    '28',
    '29',
    '30',
    '31',
    '32',
    '33',
    '34',
    '35',
    '36',
    '37',
    '38',
    '39',
    '40',
    '41',
    '42',
    '43',
    '44',
    '45',
    '46',
    '47',
    '48',
    '49',
    '50',
    '51',
    '52',
    '53',
    '54',
    '55',
    '56',
    '57',
    '58',
    '59',
    '60',
    '61',
    '62',
    '63',
    '64',
    '65',
    '66',
    '67',
    '68',
    '69',
    '70',
    '71',
    '72',
    '73',
    '74',
    '75',
    '76',
    '77',
    '78',
    '79',
    '80',
    '81',
    '82',
    '83',
    '84',
    '85',
    '86',
    '87',
    '88',
    '89',
    '90',
    '91',
    '92',
    '93',
    '94',
    '95']

voisins = {}

voisins['01'] = ['38','73','74','39','71','69'] 
voisins['02'] = ['59','80','60','77','51','08'] 
voisins['03'] = ['42','71','58','18','23','63'] 
voisins['04'] = ['83','06','05','26','84','13'] 
voisins['05'] = ['04','26','38','73']
voisins['06'] = ['83','04']
voisins['07'] = ['48','30','84','26','38','69','43','42']
voisins['08'] = ['55','51','02']
voisins['09'] = ['31','11','66']
voisins['10'] = ['89','21','52','51','77']
voisins['11'] = ['09','31','81','34','66']
voisins['12'] = ['34','30','48','15','46','82','81']
voisins['13'] = ['30','84','83']
voisins['14'] = ['27','61','50']
voisins['15'] = ['48','43','63','19','46','12'] 
voisins['16'] = ['17','79','86','87','24']
voisins['17'] = ['85','79','16','33','24']
voisins['18'] = ['36','41','45','89','58','03','23']
voisins['19'] = ['23','87','24','46','15','63'] 
voisins['2B'] = ['2A']
voisins['2A'] = ['2B']
voisins['21'] = ['10','89','58','71','39','70','52']
voisins['22'] = ['29','56','35']
voisins['23'] = ['87','19','63','03','18','36'] 
voisins['24'] = ['17','16','87','19','46','47','33']
voisins['25'] = ['39','70','90']
voisins['26'] = ['84','04','05','38','07','30'] 
voisins['27'] = ['76','60','95','78','28','61','14']
voisins['28'] = ['27','78','91','45','41','72','61']
voisins['29'] = ['22','56']   
voisins['30'] = ['34','12','48','07','84','13'] #verif
voisins['31'] = ['65','32','82','81','11','09'] #verif
voisins['32'] = ['31','65','64','40','47','82'] #verif
voisins['33'] = ['17','24','47','40'] #verif
voisins['34'] = ['11','81','12','30'] #verif 
voisins['35'] = ['50','53','49','44','56','22'] #verif
voisins['36'] = ['37','41','18','23','87','86'] #verif
voisins['37'] = ['41','36','86','49','72'] #verif
voisins['38'] = ['05','73','01','69','07','26', '42'] # verif
voisins['39'] = ['01','71','21','70','25'] #verif
voisins['40'] = ['33','47','32','64'] #verif 
voisins['41'] = ['72','37','36','18','45','28'] #verif
voisins['42'] = ['43','69','71','03','63', '07', '38'] #verif  
voisins['43'] = ['48','07','42','63','15'] #verif
voisins['44'] = ['56','35','49','85'] #verif
voisins['45'] = ['91','77','28','41','18','58','89'] #verif
voisins['46'] = ['15','19','24','47','82','12'] #verif
voisins['47'] = ['33','40','32','82','46','24'] #verif
voisins['48'] = ['12','30','07','43','15'] #verif
voisins['49'] = ['44','53','72','37','86','79','85'] #verif
voisins['50'] = ['14','61','53','35']   
voisins['51'] = ['02','77','10','52','55','08'] 
voisins['52'] = ['21','70','88','55','51','10'] 
voisins['53'] = ['49','72','61','50','35','44'] 
voisins['54'] = ['57','67','88','55']   
voisins['55'] = ['54','88','52','51','08']  
voisins['56'] = ['29','22','35','44']   
voisins['57'] = ['67','54']    
voisins['58'] = ['03','71','21','89','45','18'] 
voisins['59'] = ['02','80','62']   
voisins['60'] = ['02','80','76','27','95','77'] 
voisins['61'] = ['14','27','28','72','53','50'] 
voisins['62'] = ['80','59']    
voisins['63'] = ['15','43','42','03','23','19'] 
voisins['64'] = ['40','32','65']    
voisins['65'] = ['64','32','31']    
voisins['66'] = ['09','11']     
voisins['67'] = ['68','88','54','57']   
voisins['68'] = ['90','70','88','67']   
voisins['69'] = ['01','71','38','42']
voisins['70'] = ['21','39','25','90','88','52'] 
voisins['71'] = ['03','42','69','01','39','21','58']
voisins['72'] = ['28','61','53','49','37','41'] 
voisins['73'] = ['74','01','38','05']   
voisins['74'] = ['73','01']     
voisins['75'] = ['92','93','94']    
voisins['76'] = ['80','60','27']    
voisins['77'] = ['89','10','51','02','60','93','91','45','94','95']
voisins['78'] = ['95','27','28','91','92']  
voisins['79'] = ['17','85','49','86','16']  
voisins['80'] = ['62','59','02','60','76']  
voisins['81'] = ['11','34','12','82','31']  
voisins['82'] = ['32','31','81','12','46','47'] 
voisins['83'] = ['13','84','04','06']  
voisins['84'] = ['13','04','26','07','30','83']  
voisins['85'] = ['44','49','79','17']   
voisins['86'] = ['36','37','49','79','16','87','17'] 
voisins['87'] = ['23','19','24','16','86','36']  
voisins['88'] = ['70','90','68','67','54','55','52']
voisins['89'] = ['58','21','10','77','45']  
voisins['90'] = ['25','70','88','68']  
voisins['91'] = ['45','28','77','78','92','94'] 
voisins['92'] = ['75','95','78','93','94','91']   
voisins['93'] = ['92','95','94','77','75']
voisins['94'] = ['77','75','92','93','91']
voisins['95'] = ['78','27','60','93','92','77']


colors = ['Red', 'Green', 'Blue', 'Yellow']

colors_of_states = {}
longueur_voisin = {}
for (k, v) in voisins.items():
    longueur_voisin[k] = [len(v)]
sorted_x = dict(sorted(longueur_voisin.items(),
                key=operator.itemgetter(1), reverse=True))


def promising(departements, color):
    for voisin in voisins.get(departements):

        color_of_neighbor = colors_of_states.get(voisin)

        if color_of_neighbor == color:

            return False

    return True


def get_color_for_state(departements):
    for color in colors:
        if promising(departements, color):
            return color

#fonction pour remplacer les None par des Black
def replace_none_with_empty_str(some_dict):
    return { k: ('Black' if v is None else v) for k, v in some_dict.items() }

def main():
    for departement in sorted_x:
        colors_of_states[departement] = get_color_for_state(departement)
        
    
    result = str(replace_none_with_empty_str(colors_of_states))

    print(result)

    #on enregistre le json
    with open('./jquery.vmap.colorsFrance.js','w') as f:
        new_value = "var couleurs = " + result
        f.write(new_value)

main()