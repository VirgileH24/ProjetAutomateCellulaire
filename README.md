# ProjetAutomateCellulaire

## Utilisation :
Au Lancement du code, Il sera demandé à l’utilisateur la taille de la grille (carré). En Sachant que la taille d’une cellule est de 10, une valeur de 600 entraine de grille de 60 par 60.
la console vous demandera ensuite de rentrer 4 listes de 4 valeurs (entre 0 et 1 sinon ca ne fonctionne pas) représentants les probabilités de transition d’un couple à un autre. 
- La première liste est celle pour les couples Noirs-Blancs
- La deuxième liste est celle pour les couples Noirs-Noirs
- La troisième liste est celle pour les couples Blancs-Noirs
- La quatrième liste est celle pour les couples Blancs-Blancs

Chaque liste est composée de la même façon :
Le premier élément est la probabilité de rester le même couple, le deuxième est la probabilité que la deuxième cellule d’un couple change, le troisième est la probabilité que les deux cellules changent et le dernier est la probabilité que la première cellule change (la somme de ces quatres proba doit faire 1).
Donc les listes sont de cette forme :
- Pour les couple Noirs-Blancs : [P(NB->NB), P(NB->NN), P(NB->BN), P(NB->BB)]
- Pour les couples Noirs-Noirs : [P(NN->NN), P(NN->NB), P(NN->BB), P(NN->NB)]
- Pour les couples Blancs-Noirs :[P(BN->BN), P(BN->BB), P(BN->NB), P(BN->NN)]
- Pour les couples Blancs-Blancs: [P(BB->BB), P(BB->BN), P(BB>NN), P(BB->NB)]

Une fois la grille apparut, 3 choix sont à votre disposition :
- Le premier est pour activer au hasard un nombre aléatoirement choisie de cellule :
- Le Second est pour lancer la simulation
- Le Dernier est pour stopper la simulation 
Vous pouvez stopper pui rependre la simulation en appuyant sur second bouton. Il est également possible de cliquer sur une cellule de la grille pour l’activer.

## Exemple 

Si vous rentrer les probabilité suivante
- "NB":[0.5,0.5,0,0],"NN":[1,0,0,0],"BN":[0.5,0,0,0.5],"BB":[1,0,0,0]
Il y aura une diffusion des cellules noirs(infecté) avec un probabilité d’infecté son autre cellule du couple de 0.5. Un couple infecté reste infecté et un couple sain reste sain.
Après une génération de cellules infecté, si la simulation est lancé on voit apparaitre des « cluster »
Ce processus est long car dans notre code nous choisissons aléatoirement un couple sur lequel la transition va être appliquer (manque de temps pour coder une façon plus efficace de choisir ce couple
