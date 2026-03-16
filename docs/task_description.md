# Uzdevuma nostādne
Šis darbs ļauj studējošajiem pielietot praksē iegūtās zināšanas par pārmeklēšanā sakņotu problēmu risināšanu, izstrādājot spēles programmatūru. Praktiskā darba ietvaros studējošajiem ir jāizstrādā deterministiskā divpersonu spēle ar pilnu informāciju, kurā dators spēlē pret cilvēku. Studentu komanda var brīvi izvēlēties programmēšanas valodu vai vidi programmatūras izstrādei.

### Realizējamā spēle
Darba izpildei studējošo komanda saņem no mācībspēka spēles aprakstu. 

Komanda drīkst mainīt spēles nosacījumus. Izmaiņas ir jāievieš it īpaši gadījumos, kad spēles laikā tiek iegūts stāvoklis, kas nav atrunāts sākotnējā spēles aprakstā, vai arī pie kaut kādiem nosacījumiem nav iespējams sasniegt definēto spēles beigu stāvokli. Spēles nosacījumus var arī mainīt gadījumos, ja sākotnējais spēles apraksts noved pie vienkārša spēles koka, kura var pilnībā ģenerēt, un līdz ar to nav iespējams apmierināt praktiskā darba prasības pret heiristiskā novērtējuma funkcijas izstrādi.

### Veicamie uzdevumi
Programmatūrā obligāti ir jānodrošina šādas iespējas lietotājam: 

* izvēlēties, kurš uzsāk spēli: cilvēks vai dators;
* izvēlēties, kuru algoritmu izmantos dators konkrētajā spēles reizē: Minimaksa algoritmu vai Alfa-beta algoritmu;
* izpildīt gājienus un redzēt izmaiņas spēles laukumā pēc gājienu (gan cilvēka, gan datora) izpildes;
* uzsākt spēli atkārtoti pēc kārtējās spēles pabeigšanas.

Programmatūrai ir jānodrošina grafiskā lietotāja saskarne (komandrindiņas spēles netiks pieņemtas). Šajā gadījumā runa nav par sarežģītu, 3D grafisko saskarni, bet gan par vizuālu elementu tādu kā izvēlnes, pogas, teksta lauki, ikonas, saraksti, u.c. izmantošanu. 

Izstrādājot programmatūru, studentu komandai obligāti ir jārealizē:

* spēles koka daļas glabāšana datu struktūras veidā (klases, saistītie saraksti, utt.). Netiks pieņemti un vērtēti darbi, kuros datu struktūra netiks izveidota, bet tā vietā tiks izmantots mainīgo kopums;
spēles koka ģenerēšana līdz noteiktajam līmenim atkarībā no spēles sarežģītības un studentu komandai pieejamiem skaitļošanas resursiem;
* heiristiskā novērtējuma funkcijas izstrāde un tās pielietošana laikā, kad datoram ir jāveic gājiens;
* Minimaksa algoritms un Alfa-beta algoritms (abiem ir jābūt realizētiem kā Pārlūkošana uz priekšu pār n-gājieniem);
* 10 eksperimenti ar katru no algoritmiem, fiksējot datora un cilvēka uzvaru skaitu, datora ģenerēto un novērtēto virsotņu skaitu, datora vidējo laiku gājiena izpildei.

Praktiskajā darbā nav izvirzīta prasība lietotāja saskarnē vizuāli atspoguļot spēles koku. Spēles kokam ir jābūt atspoguļotajam datu struktūrā, kuru apstrādā spēles algoritms, lai dators varētu veikt gājienus spēlē.

Tādējādi, izstrādājot darbu, studējošo komandai ir jāizpilda šādi soļi:

1. jāsaņem spēle no mācībspēka;
2. brīvi jāizvēlas programmēšanas vide/valoda;
3. jāizveido datu struktūra spēles stāvokļu glabāšanai;
4. jāprojektē, jārealizē un jātestē spēles algoritmi;
5. jāveic eksperimenti ar abiem algoritmiem;
6. jāsagatavo atskaite par izstrādāto spēli un tā ir jāiesniedz e-studiju kursā;
7. jāveic komandas dalībnieku savstarpējā vērtēšana;
8. jāpiesakās aizstāvēšanas laikam;
9. jāaizstāv izstrādātais darbs.
