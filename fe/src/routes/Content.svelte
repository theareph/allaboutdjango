<script>
    import { onMount } from "svelte";
    const devlogs = $state([])
    const devlogMeta = $state({
        "next": null,
        "previous": null,
    })
    onMount(async () => {
        const response = await fetch("http://localhost:8000/api/devlogs/")
        const data = await response.json()
        data.results.forEach(
            item => devlogs.push(item)
        )
        devlogMeta.next = data.next
        devlogMeta.previous = data.previous

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
    <button>Next Page</button>
    {/if}
    {#if devlogMeta.previous}
    <button>Previous Page</button>
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