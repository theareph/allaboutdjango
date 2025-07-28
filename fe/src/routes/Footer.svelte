<script>
    let distro = $state("loading...")
    let totalVisits = $state("loading...")
    import {onMount} from "svelte"
    onMount(async () => {
        const response = await fetch("http://localhost:8000/api/server-distro/")
        const data = await response.json()
        distro = data.distro
        const response2 = await fetch("http://localhost:8000/api/visits/")
        const data2 = await response2.json()
        totalVisits = data2.visits

    })
</script>
<p>Server Distro: {distro}. Total Visits: {totalVisits}</p>