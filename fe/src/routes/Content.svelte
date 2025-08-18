<script>
    import {PUBLIC_API_BASE_URL} from "$env/static/public"
    import { onMount } from "svelte";
    const contentMeta = $state({
        "currentContent": "devlogs",
    })
    const devlogs = $state([])
    const books = $state([])
    const booksMeta = $state({
        "next": null,
        "previous": null,
    })
    const devlogMeta = $state({
        "next": null,
        "previous": null,
    })
    async function populateDevlogs (url) {
        devlogMeta.next = null
        devlogMeta.previous = null
        devlogs.splice(0, devlogs.length)
        const response = await fetch(url)
        const data = await response.json()
        data.results.forEach(
            item => devlogs.push(item)
        )
        devlogMeta.next = data.next
        devlogMeta.previous = data.previous

    }
    async function populateBooks (url) {
        booksMeta.next = null
        booksMeta.previous = null
        books.splice(0, books.length)
        const response = await fetch(url)
        const data = await response.json()
        data.results.forEach(
            item => books.push(item)
        )
        booksMeta.next = data.next
        booksMeta.previous = data.previous

    }

    onMount(async () => {
        await populateDevlogs(`${PUBLIC_API_BASE_URL}/api/devlogs/`)
        await populateBooks(`${PUBLIC_API_BASE_URL}/api/books/`)

    })

</script>
<p>
    <a href="#" onclick={() => contentMeta.currentContent = "devlogs"}>Devlogs</a>
    &nbsp;
    &nbsp;
    <a href="#" onclick={() => contentMeta.currentContent = "books"}>Books</a>
</p>
{#if contentMeta.currentContent === "devlogs"}
<div id="devlogs">
    <h1>Devlog</h1>
    {#each devlogs as log}
    <div class="devlog-entry">
    <h3>{log.title}</h3>
    {#if log.published_by }<h5>by {log.published_by}</h5>{/if}
    {log.content}<br><br>
    Published at {log.inserted_at}<br>
    Updated at {log.updated_at}<br>
    </div>
    {/each}
    {#if devlogMeta.next}
    <button onclick={async () => {await populateDevlogs(devlogMeta.next)}}>Next Page</button>
    {/if}
    {#if devlogMeta.previous}
    <button onclick={async () => {await populateDevlogs(devlogMeta.previous)}}>Previous Page</button>
    {/if}
</div>
{/if}
{#if contentMeta.currentContent === "books"}
<div id="books">
    <h1>Books</h1>
    {#each books as book}
    <div class="book-entry">
    <h3>{book.name}</h3>
    Author: {book.author}
    ISBN: {book.isbn}
    </div>
    {/each}
    {#if booksMeta.next}
    <button onclick={async () => {await populateBooks(booksMeta.next)}}>Next Page</button>
    {/if}
    {#if booksMeta.previous}
    <button onclick={async () => {await populateBooks(booksMeta.previous)}}>Previous Page</button>
    {/if}
</div>
{/if}

<style>
    #devlogs {
        border: 1px dotted;
    }
    .devlog-entry {
        border: 1px solid #000;
    }
    .book-entry {
        border: 1px solid #000;
    }

</style>