<template>
  
  <!-- Temp nav bar -->
  <nav>
    <ul> 
    <li><router-link to="/helloWorld">Home test</router-link> </li>   <!-- DO /test to go to the hello world page or click this!-->
    <li><router-link to="/profile">Profile</router-link></li>
  </ul>  
  </nav>
    <RouterView></RouterView>
 
</template>

<script setup lang="ts">



import 'bootstrap/dist/css/bootstrap.css'

</script>



<style scoped>

</style>
