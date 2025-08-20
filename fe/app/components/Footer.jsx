import React from 'react'

const Footer = async () => {
    const serverDistroResp = await fetch("http://localhost:8000/api/server-distro/", {next: {revalidate: 3600}})
    const serverDistro = (await serverDistroResp.json()).distro
  return (
      <>
      <hr />
      <div>The server is running: {serverDistro}</div>
      </>
  )
}

export default Footer