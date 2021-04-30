<template>
  <div class="generated-haiku">
    <textarea v-model="content">
    </textarea>
<!--    <b-input v-model="authorName" placeholder="your pseudonym"></b-input>-->
  </div>
</template>

<script>
  export default {
    name: "Haiku.vue",
    props: {
      "content": String
    },
    data() {
      return {

      }
    }
  }
</script>

<style scoped lang="scss">
  textarea {
    padding: 1rem;
    font-size: 2rem;
    height: 40rem;
    width: 20rem;
    border: none;
    text-align: center;
    resize: none;
    &:focus {
        outline: none;
      }
  }
</style>
