<template>

    <nav class="navbar navbar-expand-lg navbar-dark bg-dark static-top">
        <div class="container-fluid">
            <span class="navbar-brand mb-0 h1"><router-link to="/">Auction</router-link></span>
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <div class="nav-link"><router-link to="/">Home</router-link></div>
                    </li>
                    <li class="nav-item">
                        <div class="nav-link"><router-link to="/item">Add Item</router-link></div>
                    </li>

                    <li class="nav-item ml-auto">
                        <div class="nav-link"><router-link to="/profile">View Profile</router-link></div>
                    </li>

                    <li class="nav-item ml-auto">
                        <div class="nav-link"><router-link to="/logout">Logout</router-link></div>
                    </li>
                </ul>
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