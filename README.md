# 4_PR1_Riga_O365G

### Satura rādītājs
1. [Spēles apraksts](docs/game_description.md) 
2. [Uzdevuma nostādne](docs/task_description.md)
3. [Mākslīgā intelekta rīku izmantošana](docs/ai_using.md)
4. [Prasības atskaitei](docs/report_requirements.md)
5. [Nodošana un aizstāvēšana](docs/submission_and_defense.md)
6. [Vērtēšana](docs/grading.md)

### Atskaite 
* [Saite uz atskaiti](https://rtucloud1-my.sharepoint.com/my?id=%2Fpersonal%2Flevs%5Fbrezgins%5Fedu%5Frtu%5Flv%2FDocuments%2F4%5FPR1%5FRiga%5FO365G&viewid=acca6959%2D07a7%2D4efe%2D8c67%2De4f4b733cf05)

### Izmaiņas spēles sakumā noteikumos
#### 1.
Problēma:
* Spēles procesā var rasties situācija, kad jaunā stāvokļa iegūtais skaitlis vairs nedalās uz 2, 3, 4.
Šajā situācijā, spēlē nemainot pamatnoteikumus, spēle beidzas, un beigu skaitlis var būt
krietni lielāks par 10, kas ir pretrunā ar spēles nosacījumiem (spēle beidzas, kad sākuma skaitlis ir <= 10).
Kā arī spēles koks nav ļoti dziļš, kas principā var atļaut to pilnībā ģenerēt.

Risinājums:
* Pievienot papildus loģiku, kas nodrošina skaitļa pārveidošanu gadījumā, ja tas ir >= 10
un nedalās ne ar 2, ne ar 3 un ne ar 4. Nosauksim to par skaitļa “normalizāciju”. Šis risinājums
ļauj mums sasniegt skaitli 10 un beigt spēli šajā gadījumā, kā arī spēles koks sanāks krietni lielāks,
kas arī nodrošina spēles sarežģīšanu.	
* Svarīgi ir šādi momenti:
    * Punkti tiek pieskaitīti, balstoties uz skaitli *PIRMS* normalizācijas. Piemēram, cilvēks dala skaitli un sanāk
skaitlis 2209, kas nedalās ar 2, 3 vai 4. Tā kā tas ir nepāra skaitlis, pēc spēles pamatnoteikumiem
cilvēka punkti tiek palielināti par 1, un pēc tam skaitlis tiek normalizēts līdz 2210. 
#### 2. 
* Skaitļu diapazons tiek mainīts uz 2000000 līdz 3000000

### Git Workflow
```bash
git clone repository_name
cd 4_PR1_Riga_O365G
git checkout -b your-branch-name
```

* _Work on your changes, then:_

```bash
git status      # check changed files
git add .       # add all files
git commit -m "description of what have you done"
git push origin your-branch-name
```

* Then create a pull request from your branch to `main`, but don't merge!
* Nice Work!!! 🎉🥳
