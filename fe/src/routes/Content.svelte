<script>
    import { onMount } from "svelte";
    const devlogs = $state([])
    const devlogMeta = $state({
        "next": null,
        "previous": null,
    })
    async function populate_devlogs (url) {
        devlogs.splice(0, devlogs.length)
        const response = await fetch(url)
        const data = await response.json()
        data.results.forEach(
            item => devlogs.push(item)
        )
        devlogMeta.next = data.next
        devlogMeta.previous = data.previous

    }
    onMount(async () => {
        await populate_devlogs("http://localhost:8000/api/devlogs/")

    })

</script>

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
    <button onclick={async () => {await populate_devlogs(devlogMeta.next)}}>Next Page</button>
    {/if}
    {#if devlogMeta.previous}
    <button onclick={async () => {await populate_devlogs(devlogMeta.previous)}}>Previous Page</button>
    {/if}

</div>
<style>
    #devlogs {
        border: 1px dotted;
    }
    .devlog-entry {
        border: 1px solid #000;
    }
</style>