<script setup>
import HelloWorld from './components/HelloWorld.vue'
import Login from './components/login.vue'
</script>

<template>
    <router-link to="/">Home</router-link>
    <router-link to="/login">login</router-link>
   <!-- <Login></Login> -->
   <router-view></router-view>

</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
