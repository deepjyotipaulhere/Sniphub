<template>
    <div>
        <section class="hero is-medium is-success is-bold">
            <div class="hero-body">
                <div class="container">
                    <h1 class="title">
                        <i class="fa fa-check"></i>
                        Email Verified
                    </h1>
                    <h2 class="subtitle">
                        Your email has been successfully verified. You can now start using Sniphub!
                    </h2>
                    <nuxt-link :to="'/profile'" class="button is-danger">Go to Profile &nbsp; <i class="fa fa-chevron-circle-right"></i></nuxt-link>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
export default {
    head:{
        title: "Profile verified"
    },
    methods:{
        verify(){
            token=this.$route.query.key
            this.$axios.post(process.env.baseUrl+"/register")
        }
    }
}
</script>

<style>

</style>
