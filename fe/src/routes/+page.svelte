<script>
    import Header from "./Header.svelte";
    import Footer from "./Footer.svelte";
    import Content from "./Content.svelte";
    import { onMount } from "svelte";
    onMount(async () => {
        const lastVisit = localStorage.getItem("lastVisit")
        if (!lastVisit || Date.now() - parseInt(lastVisit) > 24 * 60 * 60 * 1000) {
            await fetch("http://localhost:8000/api/visits/", {method: "POST"})
            localStorage.setItem("lastVisit", Date.now().toString())
        }
    })
</script>
<Header/>
<Content />
<Footer/>