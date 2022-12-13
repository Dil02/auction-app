<script setup lang="ts">

</script>

<template>

    <nav class="navbar navbar-expand-lg navbar-dark bg-dark static-top">
        <div class="container-fluid">
            <span class="navbar-brand mb-0 h1"><router-link to="/">Auction</router-link></span>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#NavDropdown"
                aria-controls="NavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="NavDropdown">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <div class="nav-link"><router-link to="/item">Add Item</router-link></div>
                    </li>
                    <li class="nav-item ml-auto">
                        <div class="nav-link"><router-link to="/login">Login</router-link></div>
                    </li>
                    <li class="nav-item ml-auto">
                        <div class="nav-link"><router-link to="/profile">View Profile</router-link></div>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

</template>

<script setup lang="ts">

</script>

<style scoped>
a {
    text-decoration: none;
    color: inherit;
}
</style>