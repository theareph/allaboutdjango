'use client'
import React, { useEffect, useState } from 'react'


const Weather = () => {
    const [weather, setWeather] = useState({})
    const baseURL = process.env.NEXT_PUBLIC_BASE_URL
    useEffect(() => {
        async function updateWeather() {
            setWeather(await (await fetch(`${baseURL}/api/weather/`)).json())
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