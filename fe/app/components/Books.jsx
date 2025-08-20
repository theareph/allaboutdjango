'use client'
import React, { useEffect, useState } from 'react'

const Books = () => {
    const [nextPageURL, setNextPageURL] = useState(null)
    const [previousPageURL, setPreviousPageURL] = useState(null)
    const [books, setBooks] = useState([])

    const populateBooks = async (url) => {
        const resp = await fetch(url)
        const data = await resp.json()
        setBooks(data.results)
        setNextPageURL(data.next)
        setPreviousPageURL(data.previous)
    }
    useEffect(() => {
        const initBooks = async () => {
            await populateBooks(`${process.env.NEXT_PUBLIC_BASE_URL}/api/books/`) 
        }
        initBooks()
    }, [])
    const bookList = books.map(
        (book, index) => (
            <div key={index} className='border-solid border-1'>
            <span className='font-bold'>{book.name}</span>
            <br/>
            <span>by {book.author}</span>
            <br/>

            <span>ISBN: {book.isbn}</span>
            </div>
        )
    )
  return (
      <>
      {bookList}
      {nextPageURL && (<><button className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded' onClick={async () => await populateBooks(nextPageURL)}>Next Page</button><br/></>)}
      {previousPageURL && (<><button className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded' onClick={async () => await populateBooks(previousPageURL)}>Previous Page</button><br/></>)}
    </>
  )
}

export default Books