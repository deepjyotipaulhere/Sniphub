<template>
    <div>
        <div class="container">
            <br>
            <div class="columns">
                <div class="column"></div>
                <div class="column">
                    <div class="card has-shadow">
                        <div class="card-image">
                            <figure class="image is-4by3">
                            <img src="https://bulma.io/images/placeholders/1280x960.png" alt="Placeholder image">
                            </figure>
                        </div>
                        <div class="card-content">
                            <h1 class="title">Registration</h1>

                            <label for="">Enter your email</label>
                            <input class="input" type="text" placeholder="Choose email ID">
                            <br>
                            <br>
                            <label for="">Choose a password</label>
                            <input class="input" type="password" placeholder="Choose a password">
                            <br>
                            <label for="">Re-type password</label>
                            <input class="input" type="password" placeholder="Choose a password">
                            <br>
                            <br>
                            <label for="">Full Name</label>
                            <input class="input" type="text" placeholder="Enter your full name">
                            <br>
                            <br>
                            <button class="button is-fullwidth is-primary">Submit</button>
                        </div>
                    </div>
                    <br>
                    <span class="is-size-6">
                        <h1 class="has-text-centered">If you have an account, please <nuxt-link :to="'/login'">Sign in</nuxt-link></h1> 
                    </span>
                </div>
                <div class="column"></div>
            </div>
            
            <br>
        </div>
    </div>
</template>

<script>
export default {
    head:{
        title: "Register in Sniphub"
    }

}
</script>

<style>

</style>
