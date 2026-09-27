import joblib
import pandas as pd

# Load the trained model
model = joblib.load("src/house_price_model.pkl")


def predict_house_price(
    MedInc,
    HouseAge,
    AveRooms,
    AveBedrms,
    Population,
    AveOccup,
    Latitude,
    Longitude
):
    house_data = pd.DataFrame([[
        MedInc,
        HouseAge,
        AveRooms,
        AveBedrms,
        Population,
        AveOccup,
        Latitude,
        Longitude
    ]], columns=[
        "MedInc",
        "HouseAge",
        "AveRooms",
        "AveBedrms",
        "Population",
        "AveOccup",
        "Latitude",
        "Longitude"
    ])

    prediction = model.predict(house_data)

    return prediction[0]


# Example prediction
predicted_price = predict_house_price(
    MedInc=5.0,
    HouseAge=20.0,
    AveRooms=6.0,
    AveBedrms=1.0,
    Population=1000.0,
    AveOccup=3.0,
    Latitude=34.05,
    Longitude=-118.25
)

print("Predicted House Value:", predicted_price)
print("Estimated Price: $", round(predicted_price * 100000, 2))