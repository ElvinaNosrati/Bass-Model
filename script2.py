
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel("data/bmw_electric_sales.xlsx")


def bass_model(t, p, q, M):
    adoption = M * (((p + q)**2 / p) * np.exp(-(p + q) * t)) / ((1 + (q / p) * np.exp(-(p + q) * t))**2)
    return adoption


years = np.arange(0, len(data))
sales = data['Sales In Unit']


params, covariance = curve_fit(bass_model, years, sales, bounds=(0, [1, 1, 1000000]))
p_est, q_est, M_est = params


time_range = np.linspace(0, 20, 100) 
M_lucid = 500000  

predicted_sales = bass_model(time_range, p_est, q_est, M_lucid)

plt.figure(figsize=(10, 6))
plt.plot(time_range, predicted_sales, 'g-', label='Predicted Lucid Air Sales')
plt.xlabel("Years from 2024")
plt.ylabel("Sales (Units)")
plt.title("Predicted Diffusion of Lucid Air (2024 onwards)")
plt.legend()
plt.savefig('img/lucid_air_sales.png')
plt.show()

print(f"Estimated p (Innovation Rate): {p_est}")
print(f"Estimated q (Imitation Rate): {q_est}")
print(f"Estimated M (Market Size): {M_est}")


cumulative_adoption = bass_model(time_range, p_est, q_est, M_lucid)

# Calculating new adopters each year
new_adopters = np.diff(np.insert(cumulative_adoption, 0, 0)) 


plt.figure(figsize=(10, 6))
plt.plot(time_range, cumulative_adoption, 'g-', label='Cumulative Adopters (Lucid Air)')
plt.plot(time_range, new_adopters, 'b-', label='New Adopters per Year (Lucid Air)')
plt.xlabel("Years from 2024")
plt.ylabel("Number of Adopters")
plt.title("Lucid Air Adoption Prediction (Cumulative and New Adopters)")
plt.legend()
plt.savefig('img/lucid_air_adopters.png')
plt.show()


adoption_data = pd.DataFrame({
    'Year': np.arange(2024, 2024 + len(time_range)),
    'Cumulative Adopters': cumulative_adoption,
    'New Adopters': new_adopters
})
adoption_data.to_csv('data/lucid_air_adoption_prediction.csv', index=False)