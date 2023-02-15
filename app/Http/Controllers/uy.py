import networkx
import matplotlib.pyplot as plt
G = networkx.Graph()

edgelist = [('Auk_Ai','detikcom'),('blessingskyev','lilmeowwn7'),('blubybcadigital','youhaem168'),('blusheky','wbobalee'),('cherryaaa21','gyuw_'),
            ('cyellow_','tanyakanrl'),('F2aldi','setiawanjeje'),('FelmineLeisl','Askrlfess'),('flhemmingsgo','convomf'),('gojekindonesia','onyour_leo'),
            ('hrjx23','hrjx23'),('ibnu_nugraha_','jadijago'),('ikanasstan','ikanasstan'),('imamfz__','alfisyahri03_'),('imamfz__','i_m_mortal_'),
            ('imamfz__','jaemin_kyuu'),('imamfz__','Naedwechitaa'),('imamfz__','NanaEdut'),('imamfz__','Vallen_niat'),('itsmeopall','AnthonyBudiawan'),
            ('jaetencollect','n8minpage'),('Jasminyme','Jasminyme'),('jundiyk','jundiyk'),('me4yuuu','SmgMenfess2'),('meletupletups','tanyakanrl'),
            ('milktean00dle','bysouthskin'),('nagacentil','hayuningratri'),('owalahmon','Askrlfess'),('owalahmon','convomfs'),('Qu3en_L1lith','kurawa'),
            ('realmotherfvckr','keenandiya'),('rivaldiarrr','bdngfess'),('SeaBankID','acearsyady'),('ShopeePay_ID','applesjelo'),('tabul_ian','RacunBelanja'),
            ('WWNDHN','jadijago')]


G.add_edges_from(edgelist)
#print(G.number_of_nodes())
#print(G.number_of_edges())

options = {
    'node_color': 'red',
    'node_size': 50,
    'width': 2,
    'font_size' :10 

}
#subax1 = plt.subplot(221)

plt.figure(figsize=(10,10))
networkx.draw(G, with_labels=True, **options)
#plt.draw()
plt.savefig("path.png",dpi=199)
plt.show()

degree =networkx.degree_centrality(G)

for w in sorted(degree, key =  degree.get, reverse=True):
    print(w, round(degree[w],5))

closeness =networkx.closeness_centrality(G)

for z in sorted(degree, key =  degree.get, reverse=True):
    print(z, round(degree[w],5))
#plt.savefig("path.png")
