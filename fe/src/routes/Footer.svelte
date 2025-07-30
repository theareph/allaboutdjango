<script>
    import {PUBLIC_API_BASE_URL } from "$env/static/public"
    let distro = $state("loading...")
    let totalVisits = $state("loading...")
    import {onMount} from "svelte"
    onMount(async () => {
        const response = await fetch(`${PUBLIC_API_BASE_URL}/api/server-distro/`)
        const data = await response.json()
        distro = data.distro
        const response2 = await fetch(`${PUBLIC_API_BASE_URL}/api/visits/`)
        const data2 = await response2.json()
        totalVisits = data2.visits

    })
</script>
<p>Server Distro: {distro}. Total Visits: {totalVisits}</p>