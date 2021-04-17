<template>
  <div id="app">
    <UserInput></UserInput>
  </div>
</template>

<script>
import UserInput from "@/components/UserInput";

export default {
  name: 'App',
  components: {
    UserInput
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
