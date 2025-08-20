'use client'
import React, { useEffect, useState } from 'react'


const Visitor = () => {
    const [totalVisitors, setTotalVisitors] = useState(null);
    useEffect(
        () => {
            const processVisit = async () => {
                const totalVisitorResp = await fetch("http://localhost:8000/api/visits/")
                const totalVisitors = (await totalVisitorResp.json()).visits
                setTotalVisitors(totalVisitors)
                await fetch("http://localhost:8000/api/visits/", {method: "POST"})
            }
            if (!totalVisitors) {
                processVisit()
            }
        }
    )

  return (
    <div>Total Visitors: {totalVisitors}</div>
  )
}

export default Visitor