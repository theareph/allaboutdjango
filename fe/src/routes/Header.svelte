<script>
    import {PUBLIC_API_BASE_URL} from "$env/static/public"
    let location = $state("loading...")
    let condition = $state("loading...")
    let temp_c = $state("loading...")
	import { onMount } from 'svelte';

	onMount(async () => {

        document.querySelector("#github-link")?.setAttribute("href", `${PUBLIC_API_BASE_URL}/redir/github/`) 
        const response = await fetch(`${PUBLIC_API_BASE_URL}/api/weather/`)
        const json = await response.json();
        location = json.location
        condition = json.condition
        temp_c = json.temp_c
        

	});
</script>
<h3>You are from {location}. The weather is {condition}, and the temperature is {temp_c}C</h3>
<h3><a id="github-link">GitHub</a></h3>