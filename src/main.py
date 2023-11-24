# main.py
import os
import sys

# Add the app directory to the system path
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import subprocess
import httpx
import sys
from config import API_URL, API_KEY
from fastapi import FastAPI, HTTPException
from weather_data import save_to_json, process_weather_data
import asyncio


app = FastAPI()

@app.get("/weather")
async def get_weather(city: str, country: str):
    params = {
        "q": f"{city},{country}",
        "appid": API_KEY,
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(API_URL, params=params)

        if response.status_code == 200:
            weather_data = response.json()

            processed_data = process_weather_data(weather_data)

            # Save weather data to a JSON file (append mode)
            save_to_json(processed_data, "weather_data.json", append=True)

            return {"weather": processed_data}
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch weather data")


async def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <city> <country>")
        sys.exit(1)

    city = sys.argv[1]
    country = sys.argv[2]

    import uvicorn

    # Start the FastAPI src using uvicorn in the background
    uvicorn_cmd = [
        "uvicorn",
        "src.main:app",
        "--host", "127.0.0.1",
        "--port", "8000",
        "--reload",
    ]
    uvicorn_process = subprocess.Popen(uvicorn_cmd)

    try:

        # Make a request to the FastAPI src using the provided city and country
        async with httpx.AsyncClient() as client:
            response = await client.get(f"http://127.0.0.1:8000/weather?city={city}&country={country}")

            if response.status_code == 200:
                weather_data = response.json()
                # The data saving is handled within the get_weather function
            else:
                print(f"Failed to fetch weather data. Status code: {response.status_code}")
        await asyncio.sleep(120)

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function asynchronously
if __name__ == "__main__":
    asyncio.run(main())