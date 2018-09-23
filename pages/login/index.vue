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
                            <h1 class="title">Log in</h1>

                            <label for="">Email</label>
                            <input class="input" type="text" placeholder="Enter your registered email">
                            <br>
                            <br>
                            <label for="">Password</label>
                            <input class="input" type="password" placeholder="Enter password">
                            <br>
                            <br>
                            <button class="button is-fullwidth is-primary">Log in</button>
                        </div>
                    </div>
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
        title:"Sign in to Sniphub"
    }
}
</script>

<style>

</style>
