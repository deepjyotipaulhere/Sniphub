<template>
  <div>
    <section class="hero is-primary">
        <div class="hero-body">
            <div class="container">
                <h1 class="title">
                    Sniphub
                </h1>
                <h2 class="subtitle">
                    One place for all your software code snippets
                </h2>
                <nuxt-link :to="'/register'" class="button is-danger">Get Started</nuxt-link>
            </div>
        </div>
    </section>
  </div>
</template>

<script>
export default {
    head:{
        title: "Code Repo"
    }

}
</script>

<style>

</style>
