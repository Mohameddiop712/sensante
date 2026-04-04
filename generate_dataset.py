"""
Génère le dataset patients_dakar.csv conforme aux statistiques du Lab 1 SénSanté.
"""
import random
import csv

random.seed(42)

# Distributions cibles (issues du lab)
# sain: 158, paludisme: 136, grippe: 130, typhoide: 76
diagnostics_pool = (
    ["sain"] * 158 +
    ["paludisme"] * 136 +
    ["grippe"] * 130 +
    ["typhoide"] * 76
)

# Températures moyennes cibles
# grippe: 38.5, paludisme: 39.4, sain: 36.8, typhoide: 39.0
temp_params = {
    "sain":      (36.8, 0.4),
    "grippe":    (38.5, 0.4),
    "paludisme": (39.4, 0.4),
    "typhoide":  (39.0, 0.4),
}

# Symptômes : probabilité selon diagnostic
symptom_probs = {
    #              toux  fatigue maux_tete frissons nausee
    "sain":      [0.05, 0.05,   0.05,     0.05,    0.05],
    "grippe":    [0.85, 0.75,   0.60,     0.40,    0.30],
    "paludisme": [0.30, 0.90,   0.70,     0.85,    0.50],
    "typhoide":  [0.20, 0.85,   0.80,     0.50,    0.70],
}

# Régions (top 5 + 5 autres pour avoir 10 régions, ~500 patients)
# Dakar:145, Tambacounda:50, Ziguinchor:50, Thiès:49, Saint-Louis:48, reste:158
regions_pool = (
    ["Dakar"] * 145 +
    ["Tambacounda"] * 50 +
    ["Ziguinchor"] * 50 +
    ["Thiès"] * 49 +
    ["Saint-Louis"] * 48 +
    ["Kaolack"] * 32 +
    ["Diourbel"] * 30 +
    ["Louga"] * 28 +
    ["Fatick"] * 26 +
    ["Kolda"] * 42
)

random.shuffle(diagnostics_pool)
random.shuffle(regions_pool)

rows = []
for i in range(500):
    diag = diagnostics_pool[i]
    region = regions_pool[i]
    age = random.randint(5, 80)
    sexe = random.choice(["M", "F"])
    mu, sigma = temp_params[diag]
    temp = round(random.gauss(mu, sigma), 1)
    temp = max(35.5, min(41.5, temp))
    tension = random.randint(10, 14)
    probs = symptom_probs[diag]
    toux      = 1 if random.random() < probs[0] else 0
    fatigue   = 1 if random.random() < probs[1] else 0
    maux_tete = 1 if random.random() < probs[2] else 0
    frissons  = 1 if random.random() < probs[3] else 0
    nausee    = 1 if random.random() < probs[4] else 0
    rows.append([age, sexe, temp, tension, toux, fatigue, maux_tete, frissons, nausee, region, diag])

with open("data/patients_dakar.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["age","sexe","temperature","tension_sys","toux","fatigue","maux_tete","frissons","nausee","region","diagnostic"])
    writer.writerows(rows)

print("Dataset généré : data/patients_dakar.csv (500 patients)")
