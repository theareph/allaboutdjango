'use client'
import React, { useEffect, useState } from 'react'

const DevLogs = () => {
    const [nextPageURL, setNextPageURL] = useState(null)
    const [previousPageURL, setPreviousPageURL] = useState(null)
    const [posts, setPosts] = useState([])

    const populatePosts = async (url) => {
        const resp = await fetch(url)
        const data = await resp.json()
        setPosts(data.results)
        setNextPageURL(data.next)
        setPreviousPageURL(data.previous)
    }
    useEffect(() => {
        const initPosts = async () => {
            await populatePosts("http://localhost:8000/api/devlogs/")       
        }
        initPosts()
    }, [])
    const postList = posts.map(
        (p, index) => (
            <div key={index} className='border-solid border-1'>
            <span className='font-bold'>{p.title}</span>
            <p>{p.content}</p>
            <span>by {p.published_by}</span>
            <br/>
            <span>Posted at {p.inserted_at}</span>
            </div>
        )
    )
  return (
      <>
      {postList}
      {nextPageURL && (<><button className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded' onClick={async () => await populatePosts(nextPageURL)}>Next Page</button><br/></>)}
      {previousPageURL && (<><button className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded' onClick={async () => await populatePosts(previousPageURL)}>Previous Page</button><br/></>)}
    </>
  )
}

export default DevLogs