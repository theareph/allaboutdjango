<script>
    let location = $state("loading...")
    let condition = $state("loading...")
    let temp_c = $state("loading...")
	import { onMount } from 'svelte';

	onMount(async () => {
        const response = await fetch("http://localhost:8000/api/weather/")
        const json = await response.json();
        location = json.location
        condition = json.condition
        temp_c = json.temp_c

	});
</script>
<h3>You are from {location}. The weather is {condition}, and the temperature is {temp_c}C</h3>