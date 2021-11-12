# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import re

usman_aga = """
Bree susak 
Nuri kardeşlik ben bi safiyeyi öldüreyim geleyim 
Sus Bana Baba Deme Bana Baba Demee  
La susak sinan senin ne işin var burada... 
Ulan safiye! Rumelinin şişmanı osman aganın düşmanı 
Ben Usman Aga. 
Ben avrupalı yağlı pehlivan Osman Şentürk 
Neka güzel neka güzel 
Oka iyiyim oka iyiyim ki 
Oka mutluyum oka mutluyum ki oka olur yani 
Üçkağıtçı Sinan. 
Susak Sinan 
Seninle bir güreş tutalım 
Rusman aga 
Kadından taksi şoförü olmaaaaz. 
Arkadaşlar 
Ben bir Avrupalı olarak... 
Ben bir Avrupalıyım. 
Kara kızan 
Yağlı pehlivan Osman Aga 
Susak Ali Kemal 
Tepemin tasını artırma 
Nuri kardeşlik 
Sinancık 
Leylacık 
Ramazan baba 
Üçkağıtçı Safiye 
Safiyeeeee 
Ukela Safiye 
Dileeek kızımm 
Ali Kemal bana bir çay getir 
Bu Safiye ölüm sebebim olacak 
Susak sen kendini akıllı sanırsın üle mi susak 
Ben gidiyim ondan sonra geliyim 
Birinin telefonu çalar duruu 
Ben yağlı güreşçi Osman Aga 
Kızan 
Kızçe 
Kara Kızan 
Dilek susağı 
Bana bak kız senin bacaklarını kırarım. 
Çınar kerestesi 
Benimkiler mevludden mevlude 
Seyidi kaçırmışlar 
Cana geliceğine mala gelsin 
ula susak 
"""                         

sinan = """
Tırın tırın tırın 
Ben Sinan. Ünlü Türk şoförü Sinan 
Akasya Durağı ve onun değerli şoför kardeşleri. 
Eğze bak eğze. 
Adım sinan kaya. Memleket kartal kaya geldim buraya kaya kayaadın kaya yüregim yara beni anlarsanız kalmazsınız yaya 
Vicdansız Şaaaaaazımant Şaaaaanzımant. 
Gülibik Nolur beni affet. 
Hep o Şanzımant cadısı yüzünden. 
Ulan bücürük. 
Ali kefal çay getir bize 
Kaygana
Yav Arifim Tarifim Güzel Kardeşim
Eğze bak eğze
Arifim tarifim yemek tarifim 
Eşşek sıpası  
Can afacan şakraban. okkabal 
Sıpa can 
Şanzimentus Kayganayus 
Benim adim Sinan Kaya 

Kovdu beni cadi kaygana 
Peşinden de Nuri baba 
Baba baba baba 
benim adım Sinan Kaya kovdu cadı kaynana ben nerde yatacağım baba, baba, baba Buda Geliiiir Bu da Geçeeeer... iki orta bi sade hadi bana müsadee 

Böğrüme vurdular böğrüm ağrıyor karnıma vurdular karnım ağrıyor 
Dingilin çantası 
Sayfiye yenge 
Osprik aga 
Sen bana para vercen mi,vermicen mi 
Kara Cumayı dilekle evlendirecem 
Para var mı sende, para 
iki orta bir sade hadi bana müsade 
ipəəm Böcəəəm Çiçəəəm 
Yeni cocuk 
O zaman Uliyim ben uliyim uliyim 
Hadi bağalım oh oh hadi bağalım oh oh 
ficdansız şazimant şaaaaaaaziment 
adım sian kaya kısaca ekmek kadyıfı diyebilirsiniz 
can afacan şakraban arkadaşı serkan afacanlar 
"""

fato_aney = """
çırpısız seyrek 
Taş yigidim. 
istanbul'a gelince bir sosyete olmuşsan. 
Bak bak bak bak. 
Benim manyak oğlum 
Benim manyak gelinim 
Döşü kıllı herif isterem 
Jéniffer Lopéz 
Döşünün kıllarına kurban olam 
Tarlayı taşlı yerden avradı kardaşlı yerden almak lazım. 
Dohumu sağlam olsin istirem  
döşü kıllımidir? 
biye erkek bebe vereceksen haaaa
vışşşşşşşş neyy 
"""

saziment ="""
Paralara bak paralara. 
Ex-Damat. 
Sevgili damadım.
Hamile kalan Şükran kızı Hülya. 
becereksiz 
babası kılıklı 
canım damadım senin karnın açmı? 
kız gülbin kocan hakında öyle konuşma 
sinaaaan defol 
çeke çeke babasına çekdi çekim hatası 
defoooolll 
ayyyyyyyyyy canım damadım açmısın yemek hazırlıyayımmı 
"""

gulbin = """
Sinaaaaaaan. 
Sinaan. 
Daha neyi açıklıcaksın Sinaaan. 
Aslan kocam benim (Sinan bir kahramanlık veye para kazandığında) 
Ay ben naaparıım... 
Sinan kadınların peşinden koşuncannnnn haaaaaaaa... 
bu sefer seni bosuyacam sinannnn
"""

ali_kemal = """
Aslunda adım Ali Kemal ama siz bana kısaça Alpaçino Ali Kemal diyebilursunuz. 
Sinan api bile kız buldu ben hala bulamadum. 
Tamam Ramazan Babacuğum hemen. 

Haçan ben bu iti gezdurecem Nuri babacugum. 
Uyy Nuri babacuğum 
Tamam sinan abiniğum 
Trabzonspor'un Efsanesi Şenol Güneşi Tanımadızmı? 
ula bu kızlar benden niye kaçi daaa 
narinummm (Narin ona kızınca bağırınca) 
ula hamsi kafali sen nedersun ha orda 
ula hergün dayak yerim bu narinden adı gibi narin deyülki kurtar beni nuri baba... 
Nuri Babacğuuuumm Nuri Babacuğuuummm 
alpaçinooo balpaçinooo gülpaçinooo [araba yıkarken söyledigi sarkı sözü] 
uyyyyyyyyyyyyyyyyy narinüüüüüüüm hamsi kafalı uçkağitçı yalancı düenbaz sian abicummmmmmmm 
Doğan 

Lan ben seni sevmedi leng 

indiriyimmi babaa? indirimmi yenge? Döveyimmi bunu? 
Tahir Baba birini indirirken ona yılan bile dokunamaz 
"""

tahir_baba = """
Sinan sütlaçı bozuk revani 
Sinan efendi 
Döveyimmi bunu Şaziment Hanım? 
Şinan efendi yaptıkların yanına kar mı kalacak sandın dur lan salak
"""

seyit = """
Nasılsın agam 
Töbe töbe yaf 
Zeynoom 
Boy boy bebelerimiz olacak hemi 
Allah siye sabır versin 
Seni çok seviyem zeynom 
Siye almışam 
Kendimi denize atacam  
Yav aney 
Ben zeynoyu seviyem, başka avrat istemiyem. 
nasılsan arif kurban 
hııııııı anlamışam
"""

replikler = [ali_kemal, usman_aga, sinan, saziment, gulbin, fato_aney, tahir_baba, seyit]
kisiler = ["ali kemal", "usman aga", "sinan", "şaziment", "gülbin", "fato aney", "tahir baba", "seyit"]

for i in range(len(replikler)):
  replikler[i] = replikler[i].split("\n")

df = pd.DataFrame(columns=["Replikler", "Kisiler"])

for i in range(len(kisiler)):
    for j in range(len(replikler[i])):
      df = df.append({'Replikler' : replikler[i][j], 'Kisiler' : kisiler[i]}, ignore_index=True)
    df = df[df['Replikler'] != ""]
    df.reset_index(drop=True, inplace=True)

df["temizReplikler"] = df['Replikler'].copy()

for i in range(len(df)):
    df["temizReplikler"][i] = df["temizReplikler"][i].lower()
    df["temizReplikler"][i] = re.sub('[!@#’‘?.,\'$]', '', df["temizReplikler"][i])

def jaccardSimilarity(list1, list2):
  return float(len(list(set(list1).intersection(list2)))) / len(list(set(list1).union(list2)))

def recomendation_random_jaccard(girdi):
    jaccard_score_list = []

    if len(girdi.split()) > 1:
        for i in range(len(df)):
            jaccard_score_list.append(jaccardSimilarity(df["temizReplikler"][i], girdi))        
            maxIndex = jaccard_score_list.index(max(jaccard_score_list))
            recommendation = df['Replikler'][maxIndex]

        return recommendation

    else:
        if(girdi in kisiler):
            recommendation = df["Replikler"][df["Kisiler"] == girdi].sample(n=1).values[0]

            return recommendation
        else: # rastgele bir replik dondurulur
            recommendation = df["Replikler"].sample(n=1).values[0]
            
        return recommendation


# -- Streamlit --
# st.video("https://www.youtube.com/watch?v=8w1lL3DHvR8") # sinan
# st.video("https://www.youtube.com/watch?v=hKj7hXxtvLU") # ali kemal
# st.video("https://www.youtube.com/watch?v=O7TmGQzDhN8") # şaziment
st.title("Akasya Durağı")
girdi = st.text_input("Tarafını seç, karakterini tut", help="Karakterler\n\n- Ali Kemal\n- Usman Aga\n - Sinan\n- Şaziment\n- Gülbin\n- Fato Aney\n- Tahir Baba\n- Seyit")
st.write(recomendation_random_jaccard(str(girdi).lower()))

st.video("https://www.youtube.com/watch?v=5devNYg1TVs") # usman aga