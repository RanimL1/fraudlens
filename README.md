# fraudlens





\## Exploration des données (PaySim)



> \*\*PaySim est un jeu de données synthétique\*\* (simulation de transactions de paiement mobile). Des scores très élevés y sont attendus et ne préjugent pas des performances sur des données réelles.



| Question | Résultat | Conséquence pour le projet |

|---|---|---|

| Taille et déséquilibre | 6 362 620 transactions, 8 213 fraudes (0,129 %) | PR-AUC comme métrique principale, pas l'exactitude |

| Types concernés | Fraudes uniquement dans TRANSFER (4 097) et CASH\_OUT (4 116) | Les autres types ne contiennent jamais de fraude |

| Stabilité dans le temps | 743 heures, environ 11 fraudes par heure, sans tendance | Découpage temporel : train 1-480, validation 481-600, test 601-743 |

| Montants | Fraudes plus grosses (médiane 441 k contre 75 k) ; plafond à 10 M | Variable log(montant) ; métriques pondérées par le montant |

| Comptes | 99,85 % des comptes d'origine sont uniques ; les destinataires reviennent (jusqu'à 113 fois) | Fréquence par compte côté destinataire uniquement, calculée sur le passé |

