'use client'
import React, { useEffect, useState } from 'react'


const Weather = () => {
    const [weather, setWeather] = useState({})

    useEffect(() => {
        async function updateWeather() {
            setWeather(await (await fetch("http://localhost:8000/api/weather/")).json())
        }
        updateWeather()
    }, []
    )

  return (
    <div className="font-bold">
        {weather.location} is currently at {weather.temp_c}C. The weather is {weather.condition}
    </div>
  )
}

export default Weather