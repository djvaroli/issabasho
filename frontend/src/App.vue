<template>
  <div id="app">
    <Navbar></Navbar>
<!--    <TextBubble :text="'Hello and Welcome!'"></TextBubble>-->
    <UserInput></UserInput>
    <div class="app-background"></div>
  </div>
</template>

<script>
import UserInput from "@/components/UserInput";
import Navbar from "@/components/Navbar";
// import TextBubble from "@/components/TextBubble";

export default {
  name: 'App',
  components: {
    UserInput,
    Navbar,
    // TextBubble
  }
}
</script>

<style>
.app-background {
  position: absolute;
  width: 100%;
  height: 100%;
  left: 0;
  top: 0;
  background: #fff;
  z-index: -1;
}

#app {
  font-family: 'M PLUS Rounded 1c', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: $primary-color;
}
</style>
