import pprint
import operator
import json

import numpy as np


from collections import OrderedDict

pp = pprint.PrettyPrinter(indent=4)


departements = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
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

voisins['1'] = ['38','73','74','39','71','69'] 
voisins['2'] = ['59','80','60','77','51','8'] 
voisins['3'] = ['42','71','58','18','23','63'] 
voisins['4'] = ['83','6','5','26','84','13'] 
voisins['5'] = ['4','26','38','73']   
voisins['6'] = ['83','4','2B']    
voisins['7'] = ['48','30','84','26','38','69','43']
voisins['8'] = ['55','51','2','59']   
voisins['9'] = ['31','11','66']    
voisins['10'] = ['89','21','52','51','77']  
voisins['11'] = ['9','31','81','34']   
voisins['12'] = ['34','30','48','15','46','82','81']
voisins['13'] = ['30','84','83','2B']   
voisins['14'] = ['27','61','50']    
voisins['15'] = ['48','43','63','19','46','12'] 
voisins['16'] = ['17','79','86','87','24']  
voisins['17'] = ['85','79','16','33']   
voisins['18'] = ['36','41','45','89','58','3','23']
voisins['19'] = ['23','87','24','46','15','63'] 
voisins['2B'] = ['13','83','6','2A']
voisins['2A'] = ['2B']
voisins['21'] = ['10','89','58','71','39','70','52']
voisins['22'] = ['29','56','35']    
voisins['23'] = ['87','19','63','3','18','36'] 
voisins['24'] = ['17','16','87','19','46','47','33']
voisins['25'] = ['39','70','90']    
voisins['26'] = ['84','4','5','38','69','7'] 
voisins['27'] = ['76','60','95','78','28','61','14']
voisins['28'] = ['27','78','91','45','41','72','61']
voisins['29'] = ['22','56']     
voisins['30'] = ['34','12','48','7','26','84','13']
voisins['31'] = ['65','32','82','81','11','9'] 
voisins['32'] = ['31','65','64','40','47','82'] 
voisins['33'] = ['17','24','47','40']   
voisins['34'] = ['11','81','12','30']   
voisins['35'] = ['50','53','49','44','56','22']
voisins['36'] = ['37','41','18','23','87','86'] 
voisins['37'] = ['41','36','86','49','72']  
voisins['38'] = ['5','73','1','69','7','26','5']
voisins['39'] = ['1','71','21','70','25']  
voisins['40'] = ['33','47','32','64']   
voisins['41'] = ['72','37','36','18','45','28'] 
voisins['42'] = ['43','69','71','3','63']  
voisins['43'] = ['48','7','69','42','63','15'] 
voisins['44'] = ['56','35','53','49','85']  
voisins['45'] = ['91','77','28','41','18','58','89']
voisins['46'] = ['15','19','24','47','82','12'] 
voisins['47'] = ['33','40','32','82','46','24'] 
voisins['48'] = ['12','30','7','43','15']  
voisins['49'] = ['44','53','72','37','86','79','85']
voisins['50'] = ['14','61','53','35']   
voisins['51'] = ['2','77','10','52','55','8'] 
voisins['52'] = ['21','70','88','55','51','10'] 
voisins['53'] = ['49','72','61','50','35','44'] 
voisins['54'] = ['57','67','88','55']   
voisins['55'] = ['54','88','52','51','8']  
voisins['56'] = ['29','22','35','44']   
voisins['57'] = ['67','88','54']    
voisins['58'] = ['3','71','21','89','45','18'] 
voisins['59'] = ['2','80','62','8']   
voisins['60'] = ['2','80','76','27','95','77'] 
voisins['61'] = ['14','27','28','72','53','50'] 
voisins['62'] = ['80','59','2']    
voisins['63'] = ['15','43','42','3','23','19'] 
voisins['64'] = ['40','32','65']    
voisins['65'] = ['64','32','31']    
voisins['66'] = ['9','11']     
voisins['67'] = ['68','88','54','57']   
voisins['68'] = ['90','70','88','67']   
voisins['69'] = ['1','71','42','43','7','26','38']
voisins['70'] = ['21','39','25','90','88','52'] 
voisins['71'] = ['3','42','69','1','39','21','58']
voisins['72'] = ['28','61','53','49','37','41'] 
voisins['73'] = ['74','1','38','5']   
voisins['74'] = ['73','1']     
voisins['75'] = ['92','93','94']    
voisins['76'] = ['80','60','27']    
voisins['77'] = ['89','10','51','2','60','93','91']
voisins['78'] = ['95','27','28','91','92']  
voisins['79'] = ['17','85','49','86','16']  
voisins['80'] = ['62','59','2','60','76']  
voisins['81'] = ['11','34','12','82','31']  
voisins['82'] = ['32','31','81','12','46','47'] 
voisins['83'] = ['13','84','4','6','2B']  
voisins['84'] = ['13','4','26','7','30']  
voisins['85'] = ['44','49','79','17']   
voisins['86'] = ['36','37','49','79','16','87'] 
voisins['87'] = ['23','19','24','16','86']  
voisins['88'] = ['70','90','68','67','57','54','55']
voisins['89'] = ['58','21','10','77','45']  
voisins['90'] = ['25','70','88','68']  
voisins['91'] = ['45','28','77','78','92','94'] 
voisins['92'] = ['75','95','78','93']   
voisins['93'] = ['92','95','94','77']
voisins['94'] = ['77','75','92','93','91']
voisins['95'] = ['78','27','60','93','92']

colors = ['Red', 'Blue', 'Green', 'Orange', 'Pink']
colors_of_states = {}  

data = {}

json_data = json.dumps(data)

def dsatur(g):
    n = np.shape(g)[0]
    couleur = n*[0]
    
    #liste des sommets par ordre de degrés décroissants
    sommets_ord = tri_degre(g,True)
    
       
    #tant qu'il y a des sommets sans couleur    
    while 0 in couleur:
   
        #recherche du sommet à colorer, de degré de saturation maximum
        dsat = n*[0]
        degre_sat_max = 0
        sommetchoisi = sommets_ord[0]
        
        for i in sommets_ord:
            
            #si le sommet i est sans couleur
            if couleur[i]==0:

                vois = voisins(g,i)
               
                #calcul du degré de saturation du sommet i
                couleurvois = []
                for k in vois:
                    if couleur[k]>0:
                        couleurvois = couleurvois+[couleur[k]]
                dsat[i] = len(np.unique(couleurvois))
                
                #le sommet i est-il de degre de saturation maximum ?
                if dsat[i]>degre_sat_max :
                    degre_sat_max = dsat[i]
                    sommetchoisi = i
        
        #couleur des voisins du sommet choisi
        vois_sommetchoisi = les_voisins(g,sommetchoisi)
        couleurvois_sommetchoisi = []    
        for k in vois_sommetchoisi:
            couleurvois_sommetchoisi = couleurvois_sommetchoisi+[couleur[k]]        
        
        #choix de la plus petite couleur non présente chez les voisins du sommet choisi
        j=1
        while j in couleurvois_sommetchoisi:
            j=j+1
            
        #coloration du sommet choisi avec la couleur trouvée ci-dessus
        couleur[sommetchoisi]=j

    return couleur

def les_voisins(graph, i):     
    for voisin in graph.get(i):
        return voisin

def tri_degre(g):
    for unvoisin in g:
        print(g.get(0))
    
def main():     
    # for departement in departements:  
    #     print(les_voisins(voisins, departement)) 
    tri_degre(voisins)
        

main()