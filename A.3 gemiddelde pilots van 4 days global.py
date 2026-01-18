import pandas as pd

# CSV-bestand inladen
df = pd.read_csv(r"C:\Users\rosan\Downloads\4dayweek_pilots_data.csv")

# Gemiddelden berekenen per kolom
gemiddelden = df.mean(numeric_only=True).round(1)

print("Gemiddelden per variabele:")
print(gemiddelden)

# Als je ook de som of mediaan wil, kan dat zo:
sommen = df.sum(numeric_only=True)
mediaan = df.median(numeric_only=True)

print("\nSom per variabele:")
print(sommen)

print("\nMediaan per variabele:")
print(mediaan)