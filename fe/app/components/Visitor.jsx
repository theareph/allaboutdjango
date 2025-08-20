'use client'
import React, { useEffect, useState } from 'react'


const Visitor = () => {
    const [totalVisitors, setTotalVisitors] = useState(null);
    const baseURL = process.env.NEXT_PUBLIC_BASE_URL
    useEffect(
        () => {
            const processVisit = async () => {
                const totalVisitorResp = await fetch(`${baseURL}/api/visits/`)
                const totalVisitors = (await totalVisitorResp.json()).visits
                setTotalVisitors(totalVisitors)
                await fetch(`${baseURL}/api/visits/`, {method: "POST"})
            }
            processVisit()
        }, []
    )

  return (
    <div>Total Visitors: {totalVisitors}</div>
  )
}

export default Visitor