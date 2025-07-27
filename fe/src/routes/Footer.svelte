<script>
    let distro = $state("loading...")
    import {onMount} from "svelte"
    onMount(async () => {
        const response = await fetch("http://localhost:8000/api/server-distro/")
        const data = await response.json()
        distro = data.distro
    })
</script>
<p>Server Distro: {distro}</p>