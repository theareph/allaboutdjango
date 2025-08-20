'use client'
import { useState } from "react";
import DevLogs from "../components/DevLogs";
import Books from "../components/Books";

export default function Home() {
  
  const [content, setContent] = useState("devlogs")
  return (
    <>
    <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" onClick={() => setContent("devlogs")}>Devlogs</button>
    &nbsp;&nbsp;
    <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" onClick={() => setContent("books")}>Books</button>
    {content === "devlogs" && <><div>Dev logs</div><DevLogs/></>}
    {content === "books" && <><div>Books</div><Books/></>}
    </>
  );
}
