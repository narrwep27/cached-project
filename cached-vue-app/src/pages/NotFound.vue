<template>
    <div class="not-found-comp">
        <h1>Error 404:</h1>
        <h2>Oops, it looks like the page you're looking for doesn't exist.</h2>
        <router-link to="/">Click here to go back to the home page.</router-link>
    </div>
</template>

<script>
export default {
    name: 'NotFound'
}
</script>