import networkx
import matplotlib.pyplot as plt
import sys
import json
import ast
import base64
G = networkx.Graph()


xxx= base64.b64decode(json.dumps(sys.argv[-1]))
alist = json.loads(xxx)
edgelist=[]


for i in alist:
    
    edgelist.append((i["Username"],i["Reply"]))
    
   
#print(edgelist)

#exit()

#aww = [('Auk_Ai','detikcom'),('blessingskyev','lilmeowwn7'),('blubybcadigital','youhaem168'),('blusheky','wbobalee'),('cherryaaa21','gyuw_'),
 #           ('cyellow_','tanyakanrl'),('F2aldi','setiawanjeje'),('FelmineLeisl','Askrlfess'),('flhemmingsgo','convomf'),('gojekindonesia','onyour_leo'),
  #          ('hrjx23','hrjx23'),('ibnu_nugraha_','jadijago'),('ikanasstan','ikanasstan'),('imamfz__','alfisyahri03_'),('imamfz__','i_m_mortal_'),
   #         ('imamfz__','jaemin_kyuu'),('imamfz__','Naedwechitaa'),('imamfz__','NanaEdut'),('imamfz__','Vallen_niat'),('itsmeopall','AnthonyBudiawan'),
    #        ('jaetencollect','n8minpage'),('Jasminyme','Jasminyme'),('jundiyk','jundiyk'),('me4yuuu','SmgMenfess2'),('meletupletups','tanyakanrl'),
     #       ('milktean00dle','bysouthskin'),('nagacentil','hayuningratri'),('owalahmon','Askrlfess'),('owalahmon','convomfs'),('Qu3en_L1lith','kurawa'),
      #      ('realmotherfvckr','keenandiya'),('rivaldiarrr','bdngfess'),('SeaBankID','acearsyady'),('ShopeePay_ID','applesjelo'),('tabul_ian','RacunBelanja'),
       #     ('WWNDHN','jadijago')]#

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
#plt.show()

dclist=[]

degree =networkx.degree_centrality(G)

for w in sorted(degree, key =  degree.get, reverse=True):
    #print(w,round(degree[w],5))

    dclist.append([w,round(degree[w],5)])

#print(dclist[-1][-1]) 
dclistfix=[] 
mindc =  dclist[-1][-1]
maxdc =  dclist[0][-1]
divbtm = maxdc-mindc

# perhitungan minmax DC
for zz in dclist:
    topdc = zz[1]-mindc
    fixdc = topdc/divbtm
    dclistfix.append(fixdc) 
    #dclistfix.append([zz[0],fixdc]) ada keyusername
   # print(fixdc)
    
#print(dclistfix)
#exit()
#print(len(dclistfix))
#exit()
cclist=[]
closeness =networkx.closeness_centrality(G)
for z in sorted(closeness, key =  closeness.get, reverse=True):
     cclist.append([z,round(closeness[z],5)])

cclistfix=[] 
mincc =  cclist[-1][-1] 
maxcc =  cclist[0][-1]
divbtmcc = maxcc-mincc


# perhitungan minmax DC
for zzz in cclist:
    topcc = zzz[1]-mincc
    fixcc = topcc/divbtmcc
    cclistfix.append(fixcc) 
    #cclistfix.append([zzz[0],fixcc]) ada keyusername
    #print(fixcc)
#print(cclistfix[2])
#exit()


final_list=[]
for i in range(0,len(cclistfix)):
    #for dc in dclist:
    #    sna = {
    #            "Username":dc[0],
    #            "Nilai": (cclistfix[i]+dclistfix[i])*0.5,
    #            }
    sna = { "Nilai": (cclistfix[i]+dclistfix[i])*0.5, "Username": dclist[i][0], "Dc": dclist[i][-1], "Cc": cclist[i][-1], "CcNormal": cclistfix[i], "DcNormal": dclistfix[i] }
    final_list.append(sna)



data = {"Data":final_list}
jsondata = json.dumps(data, indent=4, sort_keys=True, default=str)
print(jsondata)
#print(final_list)